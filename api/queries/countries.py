from pydantic import BaseModel
from queries.pool import pool


class CountriesIn(BaseModel):
    country_name: str

class CountriesOut(BaseModel):
    country_id: int
    country_name: str

class CountryRepository:
    def create_country(self, country:CountriesIn) -> CountriesOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO countries
                        (country_name)
                    VALUES
                        (%s)
                    RETURNING country_id;
                    """,
                    [
                        country.country_name,
                    ]
                )
                country_id = result.fetchone()[0]
                old_data = country.dict()
                return CountriesOut(country_id=country_id, **old_data)

    def get_country_by_name(self, country_name: str) -> CountriesOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT country_id, country_name
                        FROM countries
                        WHERE country_name = %s
                        """,
                        [country_name],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return CountriesOut(
                        country_id=record[0],
                        country_name=record[1])
        except Exception as e:
            print(e)
            return {"message": "Could not find country."}
