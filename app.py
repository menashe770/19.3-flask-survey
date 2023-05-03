responses = []

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

toolbar = DebugToolbarExtension(app)


@app.route("/")
def start_survey():
    return render_template("survey_start.html", survey=survey)


@app.route("/questions/<int:qid>")
def show_question(qid):
    question = survey.questions[qid]
    return render_template("questions.html", question=question)


@app.route("/answer")
def give_answers():
    return
