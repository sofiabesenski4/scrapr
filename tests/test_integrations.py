import app.models.google_maps_adapter as gm
import os
from app.models import TextVisitor, Webpage

def test_get_website_for_a_place_search():
    adapter = gm.GoogleMapsAdapter(os.environ["GOOGLE_MAPS_API_KEY"])
    google_places_data = adapter.places_ids({"type": "restaurant"})

    the_first_places_result = google_places_data[0]
    first_website = adapter.place_website(the_first_places_result)

    assert "http" in first_website

def test_get_website_data():
    example_url = "http://www.placecage.com"
    
    webpage = Webpage(example_url)

    visitor = TextVisitor()

    webpage_text = webpage.accept(visitor)

    assert "PlaceCage" in webpage_text
    assert "<div" not in webpage_text
