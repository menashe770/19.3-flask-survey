from flask import Flask, request, render_template, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

toolbar = DebugToolbarExtension(app)

RESPONSES_KEY = "responses"


@app.route("/")
def start_survey():
    return render_template("survey_start.html", survey=survey)


@app.route("/questions/<int:qid>")
def show_question(qid):
    question = survey.questions[qid]
    return render_template("questions.html", question=question)


@app.route("/answer")
def give_answers():
    choice = request.form["answer"]
    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses
    return redirect(f"/questions/{len(responses)}")
