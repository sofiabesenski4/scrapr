import app.models.google_maps_adapter as gm
from unittest.mock import MagicMock, patch
import os


@patch("app.models.google_maps_adapter.googlemaps.Client")
def test_places_returns_mock_data(mock_client_function_init):

    mock_client_function_init.return_value = MagicMock(
        name="mocked google maps client", **{
            "places.return_value": "some data"
        })

    adapter = gm.GoogleMapsAdapter("some-api-key")
    assert adapter.places("any query params") == "some data"

