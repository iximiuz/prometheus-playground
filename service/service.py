import os
import yaml
from flask import Flask


app = Flask(__name__)

counter = 0

with open(os.environ['SCRAPE_TAPE'], 'r') as f:
    scrapes = yaml.safe_load(f)['scrapes']


@app.route('/metrics')
def metrics():
    global counter
    resp = scrapes[min(counter, len(scrapes) - 1)]
    counter += 1
    return resp['data'], resp['status_code']

