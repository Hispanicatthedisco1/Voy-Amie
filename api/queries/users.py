from pydantic import BaseModel
from typing import Optional

class UsersIn(BaseModel):
    username: str
    password: str
    email: str
    bio: Optional[str]
    profile_pic: Optional[str]
