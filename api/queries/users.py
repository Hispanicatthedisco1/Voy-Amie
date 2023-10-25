from pydantic import BaseModel
from typing import Optional
from queries.pool import pool
from typing import Union, List


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


class AllUsersOut(BaseModel):
    user_id: int
    username: str
    email: str


class UsersInUpdate(BaseModel):
    user_id: int
    bio: Optional[str]
    profile_pic: Optional[str]


class Error(BaseModel):
    message: str


class DuplicateAccountError(ValueError):
    pass


class UserOutWithPassword(UsersOut):
    hashed_password: str


class UsersRepository:
    def create_user(
        self, user: UsersIn, hashed_password: str
    ) -> UserOutWithPassword:
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
                return UserOutWithPassword(
                    user_id=user_id,
                    hashed_password=hashed_password,
                    **old_data)

    def get(self, username: str) -> Optional[UserOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT user_id,
                        username,
                        hashed_password,
                        email,
                        bio,
                        profile_pic
                        FROM users
                        WHERE username = %s
                        """,
                        [username],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return UserOutWithPassword(
                        user_id=record[0],
                        username=record[1],
                        hashed_password=record[2],
                        email=record[3],
                        bio=record[4],
                        profile_pic=record[5])
        except Exception as e:
            print(e)
            return {"message": "Could not get user."}

    def get_all_users(self) -> Union[List[AllUsersOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT user_id, username, email
                        FROM users
                        """,
                    )
                    user_list = []
                    for record in result:
                        user = UsersOut(
                            user_id=record[0],
                            username=record[1],
                            email=record[2]
                        )
                        user_list.append(user)
                    return user_list
        except Exception as e:
            print(e)
            return {"message": "Could not get all friends"}

    def get_by_user_id(self, user_id: int) -> Optional[UsersOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT user_id, username, email, bio, profile_pic
                        FROM users
                        WHERE user_id = %s
                        """,
                        [user_id],
                    )
                    record = result.fetchone()
                    print(record)
                    if record is None:
                        return None
                    return UsersOut(
                            user_id=record[0],
                            username=record[1],
                            email=record[2],
                            bio=record[3],
                            profile_pic=record[4]
                        )
        except Exception as e:
            print(e)
            return {"message": "Could not get user."}

    def update_user(
        self, user_id: int, user: UsersInUpdate, username
    ) -> Union[UsersOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE users
                        SET bio=%s,
                        profile_pic=%s
                        WHERE user_id=%s
                        RETURNING *
                        """,
                        [
                            user.bio,
                            user.profile_pic,
                            user_id,
                        ],
                    )
                    record = result.fetchone()
                    return UsersOut(
                        user_id=record[0],
                        username=record[1],
                        email=record[2],
                        bio=record[3],
                        profile_pic=record[4]
                        )
        except Exception as e:
            print(e)
            return {"message": "Could not update user."}
