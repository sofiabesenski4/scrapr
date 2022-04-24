import googlemaps


class GoogleMapsAdapter:
    def __init__(self, api_key: str):
        self.connection = googlemaps.Client(api_key)

    def __enter__(self):
        return self

    def __exit__(self):
        return

    def places_ids(self, query_params):
        places_data = self.connection.places(query_params)
        return self._extract_place_ids(places_data)

    def place_website(self, place_id):
        place_details = self.connection.place(place_id)
        site = "http://www.example.com"
        try:
            site = self._extract_website_from_place_details(place_details)
        except KeyError as err:
            print("ERROR: {0}".format(err))
        finally:
            return site

    def _extract_place_ids(self, places_response):
        return [result['place_id'] for result in places_response['results']]

    def _extract_website_from_place_details(self, places_details):
        return places_details["result"]["website"]
