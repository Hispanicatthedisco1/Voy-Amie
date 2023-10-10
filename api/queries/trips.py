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
