import googlemaps


class GoogleMapsAdapter:
    def __init__(self, api_key: str):
        self.connection = googlemaps.Client(api_key)

    def __enter__(self):
        return self

    def __exit__(self):
        return

    def places(self, query_params):
        return self.connection.places(query_params)
