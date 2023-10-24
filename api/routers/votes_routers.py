from fastapi import (
    Depends,
    APIRouter,
    Request,
    Response,
    HTTPException,
    status,
)
from authenticator import authenticator
from jwtdown_fastapi.authentication import Token
from pydantic import BaseModel
from typing import Union, List
from queries.votes import (
    VoteOut,
    VotesRepository,
    Error,
    VoteIn,
    CreateVoteError,
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


@router.post("/votes", response_model=VoteOut | HttpError)
async def create_vote(
    info: VoteIn,
    request: Request,
    response: Response,
    user_data: dict = Depends(authenticator.get_current_account_data),
    repo: VotesRepository = Depends(),
):
    try:
        voter_id = user_data["user_id"]
        vote = repo.create_vote(info, voter_id=voter_id)
    except CreateVoteError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create a vote.",
        )
    return vote


@router.delete("/votes/{vote_id}", response_model=bool)
def delete_vote(
    vote_id: int,
    repo: VotesRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete_vote(vote_id)
