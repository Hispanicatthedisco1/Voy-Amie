from pydantic import BaseModel
from typing import Optional, List, Union
from queries.pool import pool


class FriendsIn(BaseModel):
    user2_id: int


class FriendsOut(BaseModel):
    friendship_id: int
    user1_id: int
    user2_id: int


class Error(BaseModel):
    message: str


class CreateFriendshipError(ValueError):
    pass


class FriendsRepository:
    def create_friend(
        self,
        friend: FriendsIn,
        user1_id: int,
    ) -> FriendsOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO friends
                        (user1_id, user2_id)
                    VALUES
                        (%s, %s)
                    RETURNING friendship_id;
                    """,
                    [
                        user1_id,
                        friend.user2_id,
                    ],
                )
                friendship_id = result.fetchone()[0]
                old_data = friend.dict()
                return FriendsOut(
                    friendship_id=friendship_id, user1_id=user1_id, **old_data
                )
