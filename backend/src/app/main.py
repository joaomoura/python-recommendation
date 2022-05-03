from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.recommendation import router as RecommendationRouter


app = FastAPI()


app.include_router(RecommendationRouter, tags=["Recommendation"], prefix="/recommendation")


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:3001",
    "localhost:3001",
    "http://localhost:3002",
    "localhost:3002",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Hello, World!"


@app.get("/ping")
def pong():
    return {"ping": "pong!"}
