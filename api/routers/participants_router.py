from fastapi import (
    Depends,
    HTTPException,
    Response,
    APIRouter,
    Request,
)
from authenticator import authenticator

from pydantic import BaseModel
from typing import Union, List
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


@router.get(
        "/participants", response_model=Union[List[ParticipantsOut], Error])
def get_all_participants(
    repo: ParticipantRepository = Depends(),
    participant_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_all_participants()
