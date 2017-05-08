import sys
import cPickle as pickle
from flask import Flask, request


class Page:
    def __init__(self):
        self.links = {}

app = Flask(__name__)


@app.route('/pickle', methods=['POST'])
def unpickle():
    try:

      data = request.stream.read()
      page = pickle.loads(data)
      print(page.links)

    except:
        print(sys.exc_info())
        pass
    return data

if __name__ == '__main__':
    app.run()
