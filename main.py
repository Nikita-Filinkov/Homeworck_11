from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidate_by_name, get_candidate_by_skill

app = Flask(__name__)

data = load_candidates_from_json()


@app.route("/")
def index():
    return render_template('index.html', candidates=data)


@app.route("/candidate/<int:uid>")
def index_id(uid):
    candidate = get_candidate(uid)
    return render_template('profile.html', candidates=candidate)


@app.route("/search/<name>")
def search_name(name):
    candidate = get_candidate_by_name(name)
    return render_template('search.html', candidates=candidate, candidate_len=len(candidate))


@app.route("/skills/<skills>")
def search_skills(skills):
    candidate = get_candidate_by_skill(skills)
    return render_template('skills.html', candidates=candidate, candidate_len=len(candidate))


app.run()
