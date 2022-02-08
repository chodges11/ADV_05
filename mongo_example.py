
from pymongo import MongoClient

def start_mongo():
    """
    start up a connection to MongoDB

    :returns: A pymongo client object, and a database object
    """

    # In production code, these would be read from a config file, or ...
    # these values should match what's in mongo_config_dev.yml
    client = MongoClient(host='localhost', port=27017)

    return client

# Now the actual code for your project

# you don't need to use dataclasses, but it saves some boilerplate!

class DirectorCollection():
    """
    class to hold movie directors, and information about them

    At this point, just a name, but it could be all sorts of other stuff
    """
    def __init__(self, mongodb):
        """
        Initialize a DirectorsCollection with the provided database
        """
        self.mongodb = mongodb  # just in case we need it
        self.dircol = mongodb.directors


    def __len__(self):
        """ number of Directors in the collection """
        return self.dircol.count()

    def add_director(self, director_id, full_name):

        new_director = {'_id': director_id,
                        'full_name': full_name,
                        }
        self.dircol.insert_one(new_director)

    def search_director(self, director_id):
        '''
        Searches for user data
        '''
        director = self.dorcol.find_one{"_id": director_id}

        return director

