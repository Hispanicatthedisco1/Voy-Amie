from pydantic import BaseModel
from typing import List, Union
from queries.pool import pool


class VoteIn(BaseModel):
    voter_id: int
    activity_id: int


class VoteOut(BaseModel):
    vote_id: int
    voter_id: int
    activity_id: int


class Error(BaseModel):
    message: str


class CreateVoteError(ValueError):
    pass


class VotesRepository:
    def get_all_votes(self) -> Union[Error, List[VoteOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT vote_id,
                        voter_id,
                        activity_id
                        FROM votes
                        """,
                    )
                    vote_list = []
                    for record in result:
                        vote = VoteOut(
                            vote_id=record[0],
                            voter_id=record[1],
                            activity_id=record[2],
                        )
                        vote_list.append(vote)
                    return vote_list
        except Exception as e:
            print(e)
            return {"message": "Could not get all votes"}
