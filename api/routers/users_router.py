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

from pydantic import BaseModel

from queries.users import (
    UsersIn,
    UsersOut,
    UsersRepository,
    DuplicateAccountError,
)

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