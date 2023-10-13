from pydantic import BaseModel
from typing import Union
from queries.pool import pool


class ParticipantsIn(BaseModel):
    user_id: int
    trip_id: int


class ParticipantsOut(BaseModel):
    participant_id: int
    user_id: int
    trip_id: int


class Error(BaseModel):
    message: str

class CreateParticipantError(ValueError):
    pass


class ParticipantRepository:
    def create_participants(self, participant: ParticipantsIn) -> Union[ParticipantsOut, Error]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db. execute(
                    """
                    INSERT INTO trip_participants
                        (user_id, trip_id)
                    VALUES
                        (%s, %s)
                    RETURNING participant_id;
                    """,
                    [
                        participant.user_id, 
                        participant.trip_id,
                    ]
                )
                participant_id = result.fetchone()[0]
                old_data = participant.dict()
                return ParticipantsOut(
                    participant_id=participant_id, **old_data
                )