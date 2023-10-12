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
    Error,
    CreateCommentError,
    )
from typing import Optional, Union, List


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
        commenter = user_data["username"]
        comment = repo.create_comment(info, commenter=commenter)
    except CreateCommentError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create a comment.",
            )
    return comment

@router.get("/comments/{comment_id}", response_model=Optional[CommentOut])
async def get_comment(
    comment_id: int,
    response: Response,
    repo: CommentsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> CommentOut:
    comment = repo.get_comment(comment_id)
    if comment is None:
        response.status_code = 404
    return comment

@router.get("/comments", response_model=Union[List[CommentOut], Error])
def get_all_comments(
    trip: int,
    repo: CommentsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_comments(trip)

@router.put("/comments/{comment_id}", response_model=Union[CommentOut, Error])
async def update_comment(
    comment_id: int,
    comment: str,
    repo: CommentsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[CommentOut, Error]:
    commenter = user_data["username"]
    return repo.update_comment(comment_id, comment)

@router.delete("/comments/{comment_id}", response_model=bool)
def delete_comment(
    comment_id: int,
    repo: CommentsRepository = Depends(),
) -> bool:
    return repo.delete_comment(comment_id)
