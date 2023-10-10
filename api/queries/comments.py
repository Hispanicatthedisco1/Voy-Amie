from pydantic import BaseModel
from typing import Optional
from queries.pool import pool


class CommentIn(BaseModel):
    comment: str


class CommentOut(BaseModel):
    comment_id: int
    commenter: str
    comment: str


class Error(BaseModel):
    message: str


class DuplicateCommentError(ValueError):
    pass

class CreateCommentError(ValueError):
    pass


class CommentsRepository:
    def create_comment(self, comment: CommentIn, commenter) -> CommentOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO comments
                        (commenter, comment)
                    VALUES
                        (%s, %s)
                    RETURNING comment_id;
                    """,
                    [
                        commenter,
                        comment.comment,
                    ],
                )
                comment_id = result.fetchone()[0]
                old_data = comment.dict()
                return CommentOut(comment_id=comment_id, commenter=commenter, **old_data)
