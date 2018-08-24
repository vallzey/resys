from pymongo import MongoClient


def _connect_mongo(host, port, username, passwd, db):
    """ A util for making a connection to mongo """
    if username and passwd:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, passwd, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn



