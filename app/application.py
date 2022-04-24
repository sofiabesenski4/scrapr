from flask import Flask, render_template, redirect, url_for, request 
import os
from views import QueryForm
from models import GoogleMapsAdapter, TextVisitor, Webpage 
import numpy as np
import csv

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]


# from flask_wtf import FlaskForm
# from wtforms import StringField
WTF_CSRF_ENABLED = False


@app.route('/', methods=['GET', 'POST'])
def search():
    form = QueryForm(meta={'csrf': False})
    if form.validate_on_submit():
        return redirect(url_for(".results", place_type=form.business_type.data))
    return render_template('search.html', form=form)


@app.route('/results', methods=['GET'])
def results():
    place_type = request.args['place_type'] 
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

    return render_template('results.html', query_params=query_params, data=data)

def save_results_to_file(data):
    with open('test.csv', 'w', newline='') as csvfile:
        tempwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for url, contents in data.items():
            tempwriter.writerow([url, contents["text"]])

if __name__ == '__main__':
    app.run()
