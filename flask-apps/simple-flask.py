import sys
from flask import Flask, request

app = Flask(__name__)


@app.route('/py', methods=['POST'])
def post():
    try:

      data = request.stream.read()
      
      data = data + 'Py'

    except:
        print(sys.exc_info())
        pass
    return data

if __name__ == '__main__':
    app.run()
