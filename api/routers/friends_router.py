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
from queries.friends import (
    FriendsIn,
    FriendsOut,
    FriendsRepository,
    Error,
    CreateFriendshipError,
)


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/friends", response_model=FriendsOut | HttpError)
async def create_friendship(
    info: FriendsIn,
    request: Request,
    response: Response,
    user_data: dict = Depends(authenticator.get_current_account_data),
    repo: FriendsRepository = Depends(),
):
    try:
        user1_id = user_data["user_id"]
        print("PRINTING", user1_id)
        friend = repo.create_friend(info, user1_id=user1_id)
    except CreateFriendshipError:
        raise HTTPException(
            status_code=response.status_code == 404,
            detail="Could not create a friendship",
        )
    return friend


@router.delete("/friends/{friendship_id}", response_model=bool)
def delete_friend(
    friendship_id: int,
    repo: FriendsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete_friend(friendship_id)


@router.get("/friends", response_model=Union[List[FriendsOut], Error])
def get_all_friends(
    repo: FriendsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    print(user_data)
    user_id = user_data["user_id"]
    return repo.get_all_friends(user_id=user_id)
