from fastapi import (
    Depends,
    Response,
    APIRouter,
    Request,
)


from pydantic import BaseModel

from queries.countries import (
    CountriesIn,
    CountriesOut,
    CountryRepository,

)
from typing import Optional


class CountryForm(BaseModel):
    country_name: str




class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/countries")
async def create_country(
    country: CountriesIn,
    repo: CountryRepository = Depends(),
) -> CountriesOut:
    return repo.create_country(country)

@router.get("/countries/")
async def get_country_by_name(
    country_name: str,
    response: Response,
    repo: CountryRepository = Depends(),
):
    country = repo.get_country_by_name(country_name)
    if country is None:
        response.status_code = 404
    return country
