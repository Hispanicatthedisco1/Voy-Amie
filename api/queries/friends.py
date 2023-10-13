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

    def get_all_friends(self, user_id) -> Union[Error, List[FriendsOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT friendship_id, user1_id, user2_id
                        FROM friends
                        WHERE user1_id=%s OR user2_id=%s
                        """,
                        [user_id, user_id],
                    )
                    friend_list = []
                    for record in result:
                        friend = FriendsOut(
                            friendship_id=record[0],
                            user1_id=record[1],
                            user2_id=record[2],
                        )
                        friend_list.append(friend)
                    return friend_list
        except Exception as e:
            print(e)
            return {"message": "Could not get all friends"}
