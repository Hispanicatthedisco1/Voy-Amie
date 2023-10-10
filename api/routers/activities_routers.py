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

from typing import Union, List


router = APIRouter()


@router.post("/activity")
def create_activity(
    activity: ActivitiesIn,
    repo: ActivitiesRespository = Depends(),
) -> Union[Error, ActivitiesOut]:
    return repo.create_activity(activity)


@router.get("/activities", response_model=Union[List[ActivitiesOut], Error])
async def get_all_activities(
    activity_data: dict = Depends(authenticator.get_current_account_data),
    repo: ActivitiesRespository = Depends(),
): 
    return repo.get_all_activities()