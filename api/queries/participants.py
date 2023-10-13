from pydantic import BaseModel
from typing import Union, List
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


    def delete_participant(self, participant_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM trip_participants
                        WHERE participant_id=%s
                        """,
                        [participant_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False


    def get_all_participants(self) -> Union[Error, List[ParticipantsOut]]:
        try: 
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = """
                        SELECT participant_id, user_id, trip_id
                        FROM trip_participants
                        ORDER BY participant_id
                        """
                    db.execute(result)
                    records = db.fetchall()
                    
                    return [ParticipantsOut(
                            participant_id=record[0],
                            user_id=record[1],
                            trip_id=record[2],
                        )
                        for record in records
                    ]    
                   
        except Exception as e:
            print(e)
            return {"message": "Could not get all trip participants"}
