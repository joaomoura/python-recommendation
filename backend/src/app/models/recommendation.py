from typing import Optional
from typing import List
from pydantic import BaseModel, Field


class RecommendationSchema(BaseModel):
    name: str = Field(...)
    knows: List[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "knows": ["id01", "id02", "id03"]
            }
        }


class UpdateRecommendationModel(BaseModel):
    name: Optional[str]
    knows: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "knows": ["id01", "id02", "id03"]
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
