from pydantic import BaseModel
from typing import Union, List
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
            

    def get_all_activities(self) -> Union[Error, List[ActivitiesOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = """
                        SELECT activity_id,
                            trip,
                            title,
                            url,
                            date,
                            time,
                            status,
                            vote
                        FROM activities
                        ORDER BY activity_id
                    """
                    db.execute(result)
                    records = db.fetchall()
                    return [
                        ActivitiesOut(
                            activity_id=record[0],
                            trip=record[1],
                            title=record[2],
                            url=record[3],
                            date=record[4],
                            time=record[5],
                            status=record[6],
                            vote=record[7],
                        )
                        for record in records
                    ]
        except Exception as e:
            print(e)
            return {"message": "Unable to get an activities list"}
