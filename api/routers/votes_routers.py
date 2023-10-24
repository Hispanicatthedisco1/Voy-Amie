from fastapi import (
    Depends,
    APIRouter,
)
from authenticator import authenticator
from jwtdown_fastapi.authentication import Token
from pydantic import BaseModel
from typing import Union, List
from queries.votes import (
    VoteOut,
    VotesRepository,
    Error,
)


class HttpError(BaseModel):
    detail: str


class VoteToken(Token):
    vote: VoteOut


router = APIRouter()


@router.get("/votes", response_model=Union[List[VoteOut], Error])
def get_all_votes(
    repo: VotesRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_all_votes()
