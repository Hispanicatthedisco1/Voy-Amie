from fastapi import APIRouter, Depends
from queries.users import UsersIn, UsersRepository

router = APIRouter()

@router.post("/users")
def create_user(
    users:UsersIn,
    repo:UsersRepository = Depends()
    ):
    return repo.create_user(users)
