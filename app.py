'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''

from flask import Flask, render_template, abort
app = Flask(__name__)


class location:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

location = (
    location('uh',      'Uhill',   35.9679149, -78.9522732),
    # location('stanley', 'Stanley Middle',            37.8884474, -122.1155922),
    # location('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063)
)
locations_by_key = {location.key: location for location in location}


@app.route("/")
def index():
    return render_template('index.html', locations=location)


@app.route("/<location_name>")
def show_location(location_name):
    location = locations_by_key.get(location_name)
    if location:
        return render_template('map.html', location=location)
    else:
        abort(404)

app.run(host='localhost', debug=True)