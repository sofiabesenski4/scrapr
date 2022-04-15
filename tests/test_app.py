from app.application import app


def test_index_view():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert b"Form goes here!" in response.data
