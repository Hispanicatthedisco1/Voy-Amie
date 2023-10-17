from fastapi import (
    Depends,
    Response,
    APIRouter,
)

from authenticator import authenticator


from queries.activities import (
    ActivitiesIn,
    ActivitiesOut,
    ActivitiesRespository,
    Error,
)

from typing import Union, List, Optional


router = APIRouter()


@router.post("/activity")
def create_activity(
    activity: ActivitiesIn,
    repo: ActivitiesRespository = Depends(),
    activity_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, ActivitiesOut]:
    return repo.create_activity(activity)


@router.get("/activities", response_model=Union[List[ActivitiesOut], Error])
async def get_all_activities(
    activity_data: dict = Depends(authenticator.get_current_account_data),
    repo: ActivitiesRespository = Depends(),
):
    return repo.get_all_activities()


@router.get(
        "/activities/{activity_id}", response_model=Optional[ActivitiesOut])
def get_one_activity(
    activity_id: int,
    response: Response,
    activity_data: dict = Depends(authenticator.get_current_account_data),
    repo: ActivitiesRespository = Depends(),
) -> ActivitiesOut:
    activity = repo.get_one_activity(activity_id)
    if activity is None:
        response.status_code = 404
    return activity


@router.put(
        "/activities/{activity_id}",
        response_model=Union[ActivitiesOut, Error])
def update_activity(
    activity_id: int,
    activity: ActivitiesIn,
    activity_data: dict = Depends(authenticator.get_current_account_data),
    repo: ActivitiesRespository = Depends(),
) -> Union[ActivitiesOut, Error]:
    return repo.update_activity(activity_id, activity)


@router.delete("/activities/{activities_id}", response_model=bool)
def delete_activity(
    activity_id: int,
    activity_data: dict = Depends(authenticator.get_current_account_data),
    repo: ActivitiesRespository = Depends(),
) -> bool:
    return repo.delete_activity(activity_id)
