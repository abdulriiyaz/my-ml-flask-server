from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
#send a json response with hello_worlds
   return 'hey'

if __name__ == '__main__':
   app.run(debug=True)