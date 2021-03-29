import flask
import scraper
from flask import request, Response
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Scraper v2</h1><p>This site is a prototype API for a job posting scraper</p>"

@app.route('/api/v1/indeed', methods=['GET'])
def scrape_api():
    # Fort Knox level security ☜(⌒▽⌒)☞
    if "job" in request.args:
        area = charRep(request.args['area'])
        # API URL - http://127.0.0.1:5000/api/v1/indeed?job=javascript&area=Cape+Town%2C+Western+Cape&start=10
        url = f"https://za.indeed.com/jobs?q={str(request.args['job'])}&l={str(area)}&start={str(request.args['start'])}"
        json_output = json.dumps(scraper.scrape(url))
        return Response(json_output, mimetype="application/json")
    else:
        return "Error: No job field provided. Please specify a job."

def charRep(text):
    text = text.replace(" ", "+")
    text = text.replace(",", "%2C")
    return text

app.run()