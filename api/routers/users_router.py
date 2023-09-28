from fastapi import APIRouter, Depends, Response
from queries.users import UsersIn, UsersRepository, UsersOut, Error
from typing import Union

router = APIRouter()

@router.post("/users", response_model=Union[UsersOut, Error])
def create_user(
    users:UsersIn,
    response: Response,
    repo:UsersRepository = Depends()
    ):
    response.status_code = 400
    return repo.create_user(users)
