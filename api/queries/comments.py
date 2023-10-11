from pydantic import BaseModel
from typing import Optional, Union, List
from queries.pool import pool


class CommentIn(BaseModel):
    trip: int
    comment: str


class CommentOut(BaseModel):
    comment_id: int
    trip: int
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
                        (trip, commenter, comment)
                    VALUES
                        (%s, %s, %s)
                    RETURNING comment_id;
                    """,
                    [
                        comment.trip,
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
                            SELECT comment_id, trip, commenter, comment
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
                        trip=record[1],
                        commenter=record[2],
                        comment=record[3]
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not get comment."}

    def get_comments(self, trip) -> Union[Error, List[CommentOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT comment_id, trip, commenter, comment
                        FROM comments
                        WHERE trip=%s
                        """,
                        [trip],
                    )
                    comment_list = []
                    for record in result:
                        comment = CommentOut(
                            comment_id=record[0],
                            trip=record[1],
                            commenter=record[2],
                            comment=record[3],
                        )
                        comment_list.append(comment)
                    return comment_list
        except Exception as e:
            print(e)
            return {"message": "Could not get all comments!"}
