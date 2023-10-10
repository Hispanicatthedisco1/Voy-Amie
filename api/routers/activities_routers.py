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


from queries.activities import (
    ActivitiesIn, 
    ActivitiesOut, 
    ActivitiesRespository,
    Error,
)

from typing import Union


router = APIRouter()


@router.post("/activity")
def create_activity(
    activity: ActivitiesIn,
    repo: ActivitiesRespository = Depends(),
) -> Union[Error, ActivitiesOut]:
    return repo.create_activity(activity)

