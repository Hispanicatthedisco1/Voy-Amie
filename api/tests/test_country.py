from authenticator import authenticator, MyAuthenticator
from fastapi.testclient import TestClient
from main import app
from queries.countries import CountryRepository, CountriesOut
from typing import List

client = TestClient(app)


class MockUpdateCountryRepo(CountryRepository):
    def get_all_countries(self) -> List[CountriesOut]:
        result = [
            {
                "country_id": 1,
                "country_name": "Canada"
            },
            {
                "country_id": 2,
                "country_name": "Mexico"
            },
            {
                "country_id": 3,
                "country_name": "USA"
            },
            {
                "country_id": 4,
                "country_name": "France"
            }
        ]

        return result


class MockAuthenticator(MyAuthenticator):
    def try_get_current_account_data(self):
        mock_account_data = {
            "access_token": "mock_access_token",
            "type": "Bearer",
            "user": "user",
        }
        return mock_account_data


def get_fake_account_data():
    return {}


def test_get_all_countries():
    app.dependency_overrides[CountryRepository] = MockUpdateCountryRepo
    current_account_data = authenticator.get_current_account_data
    app.dependency_overrides[current_account_data] = get_fake_account_data

    json = [
        {
            "country_id": 1,
            "country_name": "Canada"
        },
        {
            "country_id": 2,
            "country_name": "Mexico"
        },
        {
            "country_id": 3,
            "country_name": "USA"
        },
        {
            "country_id": 4,
            "country_name": "France"
        }
    ]

    expected = [
        {
            "country_id": 1,
            "country_name": "Canada"
        },
        {
            "country_id": 2,
            "country_name": "Mexico"
        },
        {
            "country_id": 3,
            "country_name": "USA"
        },
        {
            "country_id": 4,
            "country_name": "France"
        }
    ]

    response = client.get("/countries/", json=json)
    print(response.json())

    assert response.status_code == 200
    assert response.json() == expected
