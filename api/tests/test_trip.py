from fastapi.testclient import TestClient
from main import app
from queries.trips import TripsRepository
from authenticator import authenticator, MyAuthenticator

client = TestClient(app)


class EmptyTripsRepository:
    def get_all_trips(self, planner):
        return [
            {
                "trip_id": 1,
                "planner": "string",
                "trip_name": "NYC TRIP",
                "city": "New York",
                "country": "string",
                "start_date": "string",
                "end_date": "string",
            },
            {
                "trip_id": 2,
                "planner": "string",
                "trip_name": "LA Trip",
                "city": "LA",
                "country": "string",
                "start_date": "string",
                "end_date": "string",
            },
        ]


class MockAuthenticator(MyAuthenticator):
    def try_get_current_account_data(self, request):
        mock_account_data = {
            "access_token": "mock_access_token",
            "type": "Bearer",
            "user": "user",
        }
        return mock_account_data


def get_fake_account_data():
    return {"username": "user123"}


def test_get_trips():
    # Arrange
    app.dependency_overrides[TripsRepository] = EmptyTripsRepository
    current_account_data = authenticator.get_current_account_data
    app.dependency_overrides[current_account_data] = get_fake_account_data

    response = client.get("/trips")

    # Act
    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == [
        {
            "trip_id": 1,
            "planner": "string",
            "trip_name": "NYC TRIP",
            "city": "New York",
            "country": "string",
            "start_date": "string",
            "end_date": "string",
        },
        {
            "trip_id": 2,
            "planner": "string",
            "trip_name": "LA Trip",
            "city": "LA",
            "country": "string",
            "start_date": "string",
            "end_date": "string",
        },
    ]
