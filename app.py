from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
   data = ('a','b','c','d')
   return json.dumps(data)

if __name__ == '__main__':
   app.run(debug=True)
