from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database import (
    add_recommendation,
    delete_recommendation,
    retrieve_knows_l1,
    retrieve_knows_l2,
    retrieve_recommendation,
    retrieve_recommendations,
    update_recommendation,
)
from app.models.recommendation import (
    ErrorResponseModel,
    ResponseModel,
    RecommendationSchema,
    UpdateRecommendationModel,
)

router = APIRouter()


@router.post("/", response_description="Recommendation data added into the database")
async def add_recommendation_data(recommendation: RecommendationSchema = Body(...)):
    recommendation = jsonable_encoder(recommendation)
    new_recommendation = await add_recommendation(recommendation)
    if new_recommendation:
        return ResponseModel(new_recommendation, "Recommendation added successfully.")
    return ErrorResponseModel("An error occurred.", 404, "Recommendation not added.")


@router.get("/", response_description="Recommendations retrieved")
async def get_recommendations():
    recommendations = await retrieve_recommendations()
    if recommendations:
        return ResponseModel(recommendations, "Recommendations data retrieved successfully")
    return ResponseModel(recommendations, "Empty list returned")


@router.get("/{id}", response_description="Recommendation data retrieved")
async def get_recommendation_data(id):
    recommendation = await retrieve_recommendation(id)
    if recommendation:
        return ResponseModel(recommendation, "Recommendation data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Recommendation doesn't exist.")


@router.get("/{id}/kl1", response_description="Knows data retrieved")
async def get_knows(id):
    knows = await retrieve_knows_l1(id)
    if knows:
        return ResponseModel(knows, "Knows data retrieved successfully")
    return ResponseModel(knows, "Empty list returned")


@router.get("/{id}/kl2", response_description="Knows data retrieved")
async def get_knows(id):
    knows = await retrieve_knows_l2(id)
    if knows:
        return ResponseModel(knows, "Knows data retrieved successfully")
    return ResponseModel(knows, "Empty list returned")


@router.put("/{id}")
async def update_recommendation_data(id: str, req: UpdateRecommendationModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_recommendation = await update_recommendation(id, req)
    if updated_recommendation:
        return ResponseModel(
            "Recommendation with ID: {} update is successful".format(id),
            "Recommendation updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the recommendation data.",
    )


@router.delete("/{id}", response_description="Recommendation data deleted from the database")
async def delete_recommendation_data(id: str):
    deleted_recommendation = await delete_recommendation(id)
    if deleted_recommendation:
        return ResponseModel(
            "Recommendation with ID: {} removed".format(
                id), "Recommendation deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Recommendation with id {0} doesn't exist".format(
            id)
    )
