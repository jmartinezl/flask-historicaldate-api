from flask import Flask
from flask import json
from flask import request
from lib.HistoricalDate import HistoricalDate

app = Flask(__name__)

historical_date = HistoricalDate()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/v2/events/today')
def today():

    data = historical_date.get_today()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/api/v2/events/random')
def random():

    data = historical_date.get_random()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/api/v2/events/date/<month>/<day>')
def calc(month='01', day='01'):

    response = None
    status = 500

    try:
        data = historical_date.get_day(month + '/' + day)
        status = 200
    except Exception as e:
        data = str(e)

    response = app.response_class(
        response=json.dumps(data),
        status=status,
        mimetype='application/json'
    )
    return response
    

if __name__ == "__main__":
    app.run(debug=True)
