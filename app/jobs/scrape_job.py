import logging
from models import GoogleMapsAdapter, TextVisitor, Webpage 
import numpy as np
import csv
import os

def scrape(place_type):
    google_connection = GoogleMapsAdapter(os.environ["GOOGLE_MAPS_API_KEY"])

    query_params = {"type": place_type}
    place_ids = np.array(google_connection.places_ids(query_params))
    top_three_place_ids = place_ids[0:3]

    urls = [google_connection.place_website(place_id)
            for place_id in top_three_place_ids]

    text_visitor = TextVisitor()
    data = {}

    for url in urls:
        webpage = Webpage(url)
        data[url] = {
            "text": webpage.accept(text_visitor)
            }

    save_results_to_file(data)

    logging.info(f"Arg was: {some_place_type} in scrape") 


def save_results_to_file(data):
    with open('test.csv', 'w', newline='') as csvfile:
        tempwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for url, contents in data.items():
            tempwriter.writerow([url, contents["text"]])
