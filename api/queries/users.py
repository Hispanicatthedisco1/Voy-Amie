from pydantic import BaseModel
from typing import Optional
from queries.pool import pool


class UsersIn(BaseModel):
    username: str
    password: str
    email: str
    bio: Optional[str]
    profile_pic: Optional[str]


class UsersOut(BaseModel):
    user_id: int
    username: str
    password: str
    email: str
    bio: Optional[str]
    profile_pic: Optional[str]

class Error(BaseModel):
    message: str


class UsersRepository:
    def create_user(self, user:UsersIn) -> UsersOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO users
                        (username, password, email, bio, profile_pic)
                    VALUES
                        (%s, %s, %s, %s, %s)
                    RETURNING user_id;
                    """,
                    [
                        user.username,
                        user.password,
                        user.email,
                        user.bio,
                        user.profile_pic
                    ]
                )
                user_id = result.fetchone()[0]
                old_data = user.dict()
                return UsersOut(user_id=user_id, **old_data)
