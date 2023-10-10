from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from authenticator import authenticator
from jwtdown_fastapi.authentication import Token
from pydantic import BaseModel
from typing import Optional
from queries.trips import (
    TripIn,
    TripOut,
    TripsRepository,
    Error,
    CreateTripError,
)


class HttpError(BaseModel):
    detail: str


class TripToken(Token):
    trip: TripOut


router = APIRouter()


@router.post("/trips", response_model=TripOut | HttpError)
async def create_trip(
    info: TripIn,
    request: Request,
    response: Response,
    user_data: dict = Depends(authenticator.get_current_account_data),
    repo: TripsRepository = Depends(),
):
    try:
        print("PRINTING:", user_data)
        planner = user_data["username"]
        trip = repo.create_trip(info, planner=planner)
    except CreateTripError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an trip",
        )
    return trip


@router.get("/trips/{trip_id}", response_model=Optional[TripOut])
def get_trip(
    trip_id: int,
    response: Response,
    repo: TripsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> TripOut:
    trip = repo.get_trip(trip_id)
    if trip is None:
        response.status_code = 404
    return trip
