import app.models.google_maps_adapter as gm
from unittest.mock import MagicMock, patch
from tests.google_api_response_samples.places_response import *


@patch("app.models.google_maps_adapter.googlemaps.Client")
def test_places_ids_returns_data(mock_client_function_init):
    mock_client_function_init.return_value = MagicMock(
        name="mocked google maps client", **{
            "places.return_value": response_dict
        })

    adapter = gm.GoogleMapsAdapter("some-api-key")
    assert "ChIJ4zu0za91j1QRhkw42Yr-aHw" in adapter.places_ids(
        "any query params")


@patch("app.models.google_maps_adapter.googlemaps.Client")
def test_place_website(mock_client_function_init):
    mock_client_function_init.return_value = MagicMock(
        name="mocked google maps client", **{
            "place.return_value": {"result": {"website": "www.test.com"}}
        })

    adapter = gm.GoogleMapsAdapter("some-api-key")
    assert adapter.place_website("some place id") == "www.test.com"
