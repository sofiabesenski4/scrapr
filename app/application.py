from flask import Flask, render_template, redirect
import os
from .views import QueryForm


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
        return redirect('/results')
    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run()
