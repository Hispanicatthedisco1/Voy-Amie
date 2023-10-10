from pydantic import BaseModel
from typing import Union
from queries.pool import pool 


class ActivitiesIn(BaseModel):
    trip: int
    title: str
    url: str
    date: str
    time: str
    status: str
    vote: int

class ActivitiesOut(BaseModel):
    activity_id: int
    trip: int
    title: str
    url: str
    date: str
    time: str
    status: str
    vote: int


class Error(BaseModel):
    message: str


class ActivitiesRespository:
    def create_activity(self, activity:ActivitiesIn) -> Union[ActivitiesOut, Error]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO activities
                        (trip, title, url, date, time, status, vote)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING activity_id;
                    """,
                    [
                        activity.trip,
                        activity.title,
                        activity.url,
                        activity.date,
                        activity.time,
                        activity.status,
                        activity.vote,
                    ]
                )
                activity_id = result.fetchone()[0]
                old_data = activity.dict()
                return ActivitiesOut(activity_id=activity_id, **old_data)