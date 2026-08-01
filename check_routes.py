import app
from werkzeug.test import Client

client = Client(app.app)
resp = client.get('/')
print(resp.status_code)
print(resp.data[:160].decode('utf-8', 'ignore'))
