import app.models.google_maps_adapter as gm
from unittest.mock import MagicMock, patch


@patch("app.models.google_maps_adapter.googlemaps.Client")
def test_places_will_call_places_on_google_client(mock_obj):
    mock_obj.return_value = MagicMock(
        name="mocked google maps client", **{
            "places.return_value": "some data"
        })

    adapter = gm.GoogleMapsAdapter("some-api-key")
    assert adapter.places("any query params") == "some data"
