from fastapi import APIRouter
from queries.users import UsersIn

router = APIRouter()

@router.post("/users")
def create_users(users:UsersIn):
    return users
