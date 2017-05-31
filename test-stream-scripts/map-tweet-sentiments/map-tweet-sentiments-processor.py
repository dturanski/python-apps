import json
import os, sys
from optparse import OptionParser
from collections import OrderedDict
from springcloudstream.stream import Processor

parser = OptionParser()

usage = "usage: %prog [options]"

parser.add_option("-c", "--categories", type="string",
                  help='Dictionary of categories{label1:minval1,label2:minval2,...}',
                  default="{'positive':0.60,'neutral':0.40,'negative':0.0}",
                  dest='categories')

options, arguments = parser.parse_args()

categories = eval(options.categories)

sentiments = {k.title(): float(v) for k, v in categories.items()}

sentiments = OrderedDict(sorted(sentiments.items(), key=lambda x: x[1]))


def label_sentiment_score(payload):
    data = json.loads(payload)
    score = data.get('polarity', -1)
    if score < 0:
        return json.dumps({'sentiment': 'Unknown'})

    first = list(sentiments)[0]
    sentiment = sentiments.get(first)

    for k in sentiments:
        if score >= sentiments.get(k):
            sentiment = k

    return json.dumps({'sentiment': sentiment})


Processor().start(label_sentiment_score)
