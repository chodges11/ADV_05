from pymongo import MongoClient


class MongoDBConnectionManager:
    """MongoDB Connection."""

    def __int__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


with MongoDBConnectionManager("192.168.86.174", 27017) as mongo:
    collection = mongo.connection.SampleDb.test
    data = collection.find({"_id": 1})
    print(data.get("name"))
