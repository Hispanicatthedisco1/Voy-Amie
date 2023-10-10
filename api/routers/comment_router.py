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
from queries.users import UsersOut
from queries.comments import (
    CommentIn,
    CommentOut,
    CommentsRepository,
    CreateCommentError,
    )


class CommentToken(Token):
    comment: CommentOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/comments", response_model=CommentOut | HttpError)
async def create_comment(
    info: CommentIn,
    request: Request,
    response: Response,
    user_data: dict = Depends(authenticator.get_current_account_data),
    repo: CommentsRepository = Depends(),
):
    try:
        comment = repo.create_comment(info)
    except CreateCommentError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create a comment.",
            )
    return comment
