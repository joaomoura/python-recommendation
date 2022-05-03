from array import array
from ast import Dict
from typing import List
from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
import os

MONGO_DETAILS = os.environ['MONGODB_CONNSTRING']

# MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.recommendations

collection = database.get_collection(
    "recommendations_collection")


# Services
def recommendation_helper(recommendation) -> dict:
    return {
        "id": str(recommendation["_id"]),
        "name": recommendation["name"],
        "knows": recommendation["knows"],
    }


# Retrieve all recommendations present in the database
async def retrieve_recommendations():
    recommendations = []
    async for recommendation in collection.find():
        recommendations.append(recommendation_helper(recommendation))
    return recommendations


# Add a new recommendation into to the database
async def add_recommendation(recommendation_data: dict) -> dict:
    knows = sanitize_duplicate_friends(recommendation_data['knows'])
    exists = await exists_all_friends(knows)
    if exists:
        recommendation_data['knows'] = knows
        recommendation = await collection.insert_one(recommendation_data)
        new_recommendation = await collection.find_one({"_id": recommendation.inserted_id})
        new_id = recommendation_helper(new_recommendation)['id']
        await fix_relationiship_after_inserted_friends(new_id, knows)
        return recommendation_helper(new_recommendation)
    return False


# Retrieve a recommendation with a matching ID
async def retrieve_recommendation(id: str) -> dict:
    recommendation = await collection.find_one({"_id": ObjectId(id)})
    if recommendation:
        return recommendation_helper(recommendation)


# Retrieve a knows with a matching ID - level 1
async def retrieve_knows_l1(id: str) -> dict:
    recommendation = await collection.find_one({"_id": ObjectId(id)})
    list = recommendation_helper(recommendation)["knows"]
    knows = await get_knows(list)
    if knows:
        return knows


# Retrieve a knows with a matching ID - level 2
async def retrieve_knows_l2(id: str) -> dict:
    recommendation = await collection.find_one({"_id": ObjectId(id)})
    knows_level1 = recommendation_helper(recommendation)["knows"]
    knows_level2 = await get_level2_filtered_Ids(id, knows_level1)
    filter_level2 = get_diff_list2_filtered_list1(knows_level2, knows_level1)
    knows = await get_knows(filter_level2)
    if knows:
        return knows


# Update a recommendation with a matching ID
async def update_recommendation(id: str, data: dict):
    if len(data) < 1:
        return False
    recommendation = await collection.find_one({"_id": ObjectId(id)})
    knows = sanitize_duplicate_friends(data['knows'])
    exist_id_itself = knows.count(id)
    if exist_id_itself:
        return False
    if recommendation:
        exists = await exists_all_friends(knows)
        if exists:
            rec_knows = recommendation_helper(recommendation)
            data['knows'] = knows
            updated_recommendation = await collection.update_one({"_id": ObjectId(id)}, {"$set": data})
            if updated_recommendation:
                await fix_relationiship_after_updated_friends(rec_knows, data)
                return True
        return False


# Delete a recommendation from the database
async def delete_recommendation(id: str):
    recommendation = await collection.find_one({"_id": ObjectId(id)})
    if recommendation:
        rec_knows = recommendation_helper(recommendation)
        await fix_relationiship_after_deleted_friends(rec_knows)
        await collection.delete_one({"_id": ObjectId(id)})
        return True


# HELPERS
def sanitize_duplicate_friends(knows):
    res = []
    [res.append(x) for x in knows if x not in res]
    return res


async def exists_all_friends(knows):
    for know in knows:
        data = await collection.find_one({"_id": ObjectId(know)})
        if data is None:
            return False
    return True


def get_diff_list2_filtered_list1(list2, list1):
    return [x for x in list2 if all(y not in x for y in list1)]


async def get_knows(filter_data):
    knows = []
    for id in filter_data:
        know = await collection.find_one({"_id": ObjectId(id)})
        knows.append(recommendation_helper(know))
    return knows


async def get_level2_filtered_Ids(id, knows_level1):
    knows_level2 = []
    for kl1 in knows_level1:
        friend = await collection.find_one({"_id": ObjectId(kl1)})
        friends = recommendation_helper(friend)["knows"]
        friends.remove(id)
        for fId in friends:
            knows_level2.append(fId)
    return knows_level2


async def fix_relationiship_after_inserted_friends(id, friends):
    if friends:
        for k in friends:
            friend = await collection.find_one({"_id": ObjectId(k)})
            knows = recommendation_helper(friend)["knows"]
            knows.append(id)
            data = {'knows': knows}
            await collection.update_one({"_id": ObjectId(k)}, {"$set": data})


async def fix_relationiship_after_updated_friends(rec_knows, data):
    leave_friends = get_diff_list2_filtered_list1(rec_knows['knows'], data['knows'])
    if leave_friends:
        for f in leave_friends:
            l_friend = await collection.find_one({"_id": ObjectId(f)})
            l_friends = recommendation_helper(l_friend)["knows"]
            l_filtered = get_diff_list2_filtered_list1(l_friends, [rec_knows['id']])
            l_data = {'knows': l_filtered}
            await collection.update_one({"_id": ObjectId(f)}, {"$set": l_data})
    for f in data['knows']:
        c_friend = await collection.find_one({"_id": ObjectId(f)})
        c_friends = recommendation_helper(c_friend)["knows"]
        c_friends.append(rec_knows['id'])
        s_friends = sanitize_duplicate_friends(c_friends)        
        c_data = {'knows': s_friends}
        await collection.update_one({"_id": ObjectId(f)}, {"$set": c_data})


async def fix_relationiship_after_deleted_friends(rec_knows):
    if rec_knows['knows']:
        for f in rec_knows['knows']:
            friend = await collection.find_one({"_id": ObjectId(f)})
            friends = recommendation_helper(friend)["knows"]
            filtered_friends = get_diff_list2_filtered_list1(friends, [rec_knows['id']])
            data = {'knows': filtered_friends}
            await collection.update_one({"_id": ObjectId(f)}, {"$set": data})
