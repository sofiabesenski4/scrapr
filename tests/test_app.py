from app.application import app


def test_search():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert b"Search" in response.data
    assert b"type" in response.data

def test_results_for_place_type():
    tester = app.test_client()
    response = tester.get(
            "/results?place_type=restaurant",
            content_type="html/text"
            )

    assert response.status_code == 200
    assert b"Query Params" in response.data
    assert b"Results" in response.data
    assert b"http" in response.data

def test_results_for_invalid_place_type():
    tester = app.test_client()
    response = tester.get(
            "/results?place_type=some_invalid_type",
            content_type="html/text"
            )
    assert response.status_code == 200

