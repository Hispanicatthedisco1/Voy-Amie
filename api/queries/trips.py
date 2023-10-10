from pydantic import BaseModel
from typing import Optional
from queries.pool import pool


class TripIn(BaseModel):
    trip_name: str
    city: str
    country: str
    start_date: str
    end_date: str


class TripOut(BaseModel):
    trip_id: int
    planner: str
    trip_name: str
    city: str
    country: str
    start_date: str
    end_date: str


class Error(BaseModel):
    message: str


class CreateTripError(ValueError):
    pass


class TripsRepository:
    def create_trip(
        self,
        trip: TripIn,
        planner,
    ) -> TripOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO trips
                        (planner, trip_name, city, country, start_date, end_date)
                    VALUES
                       (%s, %s, %s, %s, %s, %s)
                    RETURNING trip_id;
                    """,
                    [
                        planner,
                        trip.trip_name,
                        trip.city,
                        trip.country,
                        trip.start_date,
                        trip.end_date,
                    ],
                )
                trip_id = result.fetchone()[0]
                old_data = trip.dict()
                return TripOut(trip_id=trip_id, planner=planner, **old_data)

    def get_trip(self, trip_id: int) -> Optional[TripOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT trip_id, planner, trip_name, city, country, start_date, end_date
                        FROM trips
                        WHERE trip_id=%s
                        """,
                        [trip_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return TripOut(
                        trip_id=record[0],
                        planner=record[1],
                        trip_name=record[2],
                        city=record[3],
                        country=record[4],
                        start_date=record[5],
                        end_date=record[6],
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not get trip."}
