from authenticator import authenticator, MyAuthenticator
from fastapi.testclient import TestClient
from main import app
from queries.comments import CommentsRepository, CommentOut


client = TestClient(app)


class MockCommentsQueries:
    def get_comment(self, comment_id: int):
        return CommentOut(
            comment_id=1,
            trip=1,
            commenter="obiwan",
            comment="Only a Sith deals in absolutes"
        )


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


def test_get_comment():
    app.dependency_overrides[CommentsRepository] = MockCommentsQueries
    current_account_data = authenticator.get_current_account_data
    app.dependency_overrides[current_account_data] = get_fake_account_data

    response = client.get("/comments/1")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {
        "comment_id": 1,
        "trip": 1,
        "commenter": "obiwan",
        "comment": "Only a Sith deals in absolutes"
        }
