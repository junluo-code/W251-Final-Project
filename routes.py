from flask import Flask, render_template, jsonify
from cassandra.cluster import Cluster

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kpi1')
def kpi1():
    return render_template("kpi1.html")

@app.route('/kpi2')
def kpi2():
    return render_template("kpi2.html")

@app.route('/kpi3')
def kpi3():
    return render_template("kpi3.html")

@app.route('/rsvp')
def rsvp():
    return app.send_static_file("rsvps.json")


@app.route('/api/venue',  methods=['GET'])
def get_venues():
    cluster = Cluster()
    session = cluster.connect("meetup")
    venues = session.execute('SELECT * from venues')
    results = []
    for venue in venues:
        result = '{' + '"venue_id":' + venue.venue_id + ', "lat":' + venue.lat  + ', "lon":' + venue.lon + ', "venue_name": "' + venue.venue_name + '"}'
        results.append(result)
        #print venue.venue_id, venue.lat, venue.lon, venue.venue_name
    return jsonify({'results':results})
    #return jsonify({'results':venues})

if __name__ == '__main__':
    app.run()
