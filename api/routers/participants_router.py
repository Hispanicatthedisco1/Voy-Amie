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
from typing import Optional, Union, List
from queries.participants import (
    ParticipantsIn,
    ParticipantsOut,
    ParticipantRepository,
    Error,
    CreateParticipantError,
)


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/participants", response_model=ParticipantsOut | HttpError)
async def create_participants(
    info: ParticipantsIn,
    request: Request,
    response: Response,
    data: dict = Depends(authenticator.get_current_account_data),
    repo: ParticipantRepository = Depends(),
):
    try:
        participant = repo.create_participants(info)
    except CreateParticipantError:
        raise HTTPException(
            status_code=response.status_code == 404,
            detail="Could not create a participant",
        )
    return participant


@router.delete("/participants/{participant_id}", response_model=bool)
def delete_participant(
    participant_id: int,
    repo: ParticipantRepository = Depends(),
    participant_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete_participant(participant_id)
