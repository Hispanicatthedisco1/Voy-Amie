from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import (
    users_router,
    trips_router,
    activities_routers,
    comment_router,
    countries_router,
    friends_router,
    participants_router,
)
from authenticator import authenticator

app = FastAPI()
app.include_router(users_router.router)
app.include_router(comment_router.router)
app.include_router(authenticator.router)
app.include_router(trips_router.router)
app.include_router(activities_routers.router)
app.include_router(countries_router.router)
app.include_router(friends_router.router)
app.include_router(participants_router.router)

origins = ["http://localhost:3000", os.environ.get("CORS_HOST", None)]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "You hit the root path!"}


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00",
        }
    }
