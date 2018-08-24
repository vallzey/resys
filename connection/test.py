from connection.conn_mongodb import _connect_mongo

host = '127.0.0.1'
port = '27017'
username = 'testad'
passwd = 'test'
db = 'admin'

conn = _connect_mongo(host=host, port=port, username=username, passwd=passwd, db=db)
db_test = conn['test']
collections = db_test.collection_names()
print(collections)

