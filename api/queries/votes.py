from pydantic import BaseModel
from typing import List, Union
from queries.pool import pool


class VoteIn(BaseModel):
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

    def create_vote(self, vote: VoteIn, voter_id) -> VoteOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO votes
                        (voter_id, activity_id)
                    VALUES
                        (%s, %s)
                    RETURNING vote_id;
                    """,
                    [
                        voter_id,
                        vote.activity_id,
                    ],
                )
                vote_id = result.fetchone()[0]
                old_data = vote.dict()
                return VoteOut(vote_id=vote_id, voter_id=voter_id, **old_data)

    def delete_vote(self, vote_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM votes
                        WHERE vote_id=%s
                        """,
                        [vote_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False
