import app.models.google_maps_adapter as gm
import os 


def test_get_places():
    adapter = gm.GoogleMapsAdapter(os.environ["GOOGLE_MAPS_API_KEY"])
    results =  adapter.places({"type": "restaurant"})
    breakpoint()


def test_get_website_for_place():
    pass


def test_get_maps_data_for_a_place():
    pass
