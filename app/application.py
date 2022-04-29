from flask import Flask, render_template, redirect, url_for, request 
import os
from views import QueryForm

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
    with faktory.connection() as client:
        client.queue('scrape_job', args=[place_type])
    return render_template('sent scraping job!')



def save_results_to_file(data):
    with open('test.csv', 'w', newline='') as csvfile:
        tempwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for url, contents in data.items():
            tempwriter.writerow([url, contents["text"]])

if __name__ == '__main__':
    app.run()
