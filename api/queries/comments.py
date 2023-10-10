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

    def get_comment(self, comment_id: int) -> CommentOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                            """
                            SELECT comment_id, commenter, comment
                            FROM comments
                            WHERE comment_id=%s
                            """,
                            [comment_id],
                        )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return CommentOut(
                        comment_id=record[0],
                        commenter=record[1],
                        comment=record[2]
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not get comment."}
