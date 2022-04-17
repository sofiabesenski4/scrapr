from flask import Flask, render_template, redirect, url_for, session
import os
from app.views import QueryForm
from app.models import GoogleMapsAdapter
import numpy as np

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
        session["place_type"] = form.business_type.data
        return redirect(url_for(".results", place_type=form.business_type.data))
    return render_template('search.html', form=form)


@app.route('/results', methods=['GET'])
def results():
    place_type = session['place_type']
    google_connection = GoogleMapsAdapter(os.environ["GOOGLE_MAPS_API_KEY"])

    query_params = {"type": place_type}
    place_ids = np.array(google_connection.places_ids(query_params))
    top_three_place_ids = place_ids[0:3]

    data = [google_connection.place_website(
        place_id) for place_id in top_three_place_ids]
    return render_template('results.html', query_params=query_params, data=data)


if __name__ == '__main__':
    app.run()
