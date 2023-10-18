from authenticator import authenticator, MyAuthenticator
from fastapi.testclient import TestClient
from main import app
from queries.activities import ActivitiesRespository, ActivitiesIn

client = TestClient(app)


class MockUpdateActivityRepo:
    def update_activity(self, activity_id: int, activity: ActivitiesIn):
        result = {
            "activity_id": 5,
            "trip": 2,
            "title": "Going to Vegas",
            "url": "vegas.com",
            "date": "10/18/2023",
            "time": "9:00am",
            "status": "Pending",
            "vote": 0
        }
        result = {**result, **activity.dict()}
        return result


class MockAuthenticator(MyAuthenticator):
    def try_get_current_account_data(self, request):
        mock_account_data = {
            "access_token": "mock_access_token",
            "type": "Bearer",
            "user": "user",
        }
        return mock_account_data


def get_fake_account_data():
    return {}


def test_update_activity():
    app.dependency_overrides[ActivitiesRespository] = MockUpdateActivityRepo
    current_account_data = authenticator.get_current_account_data
    app.dependency_overrides[current_account_data] = get_fake_account_data

    json = {
        "activity_id": 5,
        "trip": 2,
        "title": "Driving to Vegas",
        "url": "vegas.com",
        "date": "10/20/2023",
        "time": "10:00am",
        "status": "Pending",
        "vote": 8
    }

    expected = {
        "activity_id": 5,
        "trip": 2,
        "title": "Driving to Vegas",
        "url": "vegas.com",
        "date": "10/20/2023",
        "time": "10:00am",
        "status": "Pending",
        "vote": 8
    }

    response = client.put("/activities/5", json=json)
    print(response.json())

    assert response.status_code == 200
    assert response.json() == expected
