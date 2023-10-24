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
from queries.users import UsersOut, UsersRepository, AllUsersOut
from queries.friends import (
    FriendsIn,
    FriendsOut,
    FriendsRepository,
    Error,
    CreateFriendshipError,
)


class FriendsWithUserOut(BaseModel):
    friendship_id: int
    myself: int
    friend: UsersOut


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


@router.get("/friends", response_model=Union[List[AllUsersOut], Error])
def get_all_friends(
    repo: FriendsRepository = Depends(),
    user_repo: UsersRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):

    user_id = user_data["user_id"]

    friends_list = repo.get_all_friends(user_id=user_id)
    my_friends = []

    for friend in friends_list:
        if user_id != friend.user1_id:
            user = user_repo.get_by_user_id(friend.user1_id)
        else:
            user = user_repo.get_by_user_id(friend.user2_id)
        my_friends.append(user)
    return my_friends
