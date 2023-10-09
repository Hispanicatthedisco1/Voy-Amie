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
        trip = repo.create_trip(info)
    except CreateTripError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an trip",
        )
    return trip
