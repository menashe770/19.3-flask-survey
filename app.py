responses = []

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

toolbar = DebugToolbarExtension(app)


@app.route("/")
def start_survey():
    survey = surveys["satisfaction"]
    return render_template("survey_start.html", satisfaction_survey=survey)
