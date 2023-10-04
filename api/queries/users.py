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
    email: str
    bio: Optional[str]
    profile_pic: Optional[str]

class Error(BaseModel):
    message: str

class DuplicateAccountError(ValueError):
    pass

class UserOutWithPassword(UsersOut):
    hashed_password: str


class UsersRepository:
    def create_user(self, user:UsersIn, hashed_password: str) -> UserOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO users
                        (username, hashed_password, email, bio, profile_pic)
                    VALUES
                        (%s, %s, %s, %s, %s)
                    RETURNING user_id;
                    """,
                    [
                        user.username,
                        hashed_password,
                        user.email,
                        user.bio,
                        user.profile_pic
                    ]
                )
                user_id = result.fetchone()[0]
                old_data = user.dict()
                return UserOutWithPassword(user_id=user_id, hashed_password=hashed_password, **old_data)

    def get(self, username: str) -> Optional[UserOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT user_id, username, hashed_password, email, bio, profile_pic
                        FROM users
                        WHERE username = %s
                        """,
                        [username],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return UserOutWithPassword(
                        user_id = record[0],
                        username = record[1],
                        hashed_password = record[2],
                        email = record[3],
                        bio = record[4],
                        profile_pic = record[5])
        except Exception as e:
            print(e)
            return {"message": "Could not get user."}
