
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect("meetup")
venues = session.execute('SELECT * from venues')
results = []
for venue in venues:
    #print venue.venue_id, venue.lat, venue.lon, venue.venue_name
    result = '{' + '"venue_id":' + venue.venue_id + ', "lat":' + venue.lat + ', "lon":' + venue.lon + ', "venue_name": "' + venue.venue_name + '"}'
    results.append(result)
    print result

print results

