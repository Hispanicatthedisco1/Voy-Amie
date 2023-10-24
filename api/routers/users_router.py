from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from typing import Union, List
from pydantic import BaseModel

from queries.users import (
    UsersIn,
    UsersOut,
    AllUsersOut,
    UsersRepository,
    DuplicateAccountError,
    Error,
    UserOutWithPassword,
)
from typing import Optional


class UserForm(BaseModel):
    username: str
    password: str


class UserToken(Token):
    user: UsersOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/users", response_model=UserToken | HttpError)
async def create_user(
    info: UsersIn,
    request: Request,
    response: Response,
    repo: UsersRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        user = repo.create_user(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = UserForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return UserToken(user=user, **token.dict())


@router.get("/token", response_model=UserToken | None)
async def get_token(
    request: Request,
    user: UsersIn = Depends(authenticator.try_get_current_account_data),
) -> UserToken | None:
    if user and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "user": user,
        }


@router.get("/users/{username}", response_model=Optional[UserOutWithPassword])
def get_one_user(
    username: str,
    response: Response,
    repo: UsersRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> UserOutWithPassword:
    user = repo.get(username)
    if user is None:
        response.status_code = 404
    return user


@router.get("/users/id/{user_id}", response_model=Optional[UsersOut])
def get_user(
    user_id: int,
    response: Response,
    repo: UsersRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> UsersOut:
    print("hi")
    user = repo.get_by_user_id(user_id)
    if user is None:
        response.status_code = 404
    return user


@router.get("/users", response_model=Union[List[AllUsersOut], Error])
def get_all_users(
    repo: UsersRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):

    return repo.get_all_users()
