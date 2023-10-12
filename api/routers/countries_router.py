from fastapi import (
    Depends,
    Response,
    APIRouter,
    Request,
)

from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel

from queries.countries import (
    CountriesIn,
    CountriesOut,
    CountryRepository,
    Error,

)
from typing import Union, List


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

@router.get("/countries/{country_name}")
async def get_country_by_name(
    country_name: str,
    response: Response,
    repo: CountryRepository = Depends(),
):
    country = repo.get_country_by_name(country_name)
    if country is None:
        response.status_code = 404
    return country

@router.get("/countries/", response_model=Union[List[CountriesOut], Error])
async def get_all_countries(
    activity_data: dict = Depends(authenticator.get_current_account_data),
    repo: CountryRepository = Depends(),
):
    return repo.get_all_countries()


@router.put("/countries/{countries_id}", response_model=Union[CountriesOut, Error])
def update_country(
    country_id: int,
    country: CountriesIn,
    repo: CountryRepository = Depends(),
    country_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[CountriesOut, Error]:
    # planner = country_data["country_name"]
    return repo.update_country(country_id, country,)



@router.delete("/countries/{country_id}", response_model=bool)
def delete_country(
    country_id: int,
    repo: CountryRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete_country(country_id)
