#!/usr/bin/python3

"""index """
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_views():
    """ returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False )
def stats():
    """ Retrieves the number of each objects by type """
        classes = [Amenity, City, Place, Review, State, User]
        names = ["amenities", "cities", "places", "reviews", "states", "users"]
        num_objs = {}
        for i in range(len(classes)):
            num_objs[names[i]] = storage.count(classes[i])
        return jsonify(num_objs)



if __name__ == "__main__":
        app.run(host="0.0.0.0")
