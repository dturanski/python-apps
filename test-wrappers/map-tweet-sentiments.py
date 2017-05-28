import json
from java.math import BigDecimal
#
# For testing, the module is not __main__ at runtime
#
if __name__ == "__main__":
    from java.util import HashMap
    from java.math import BigDecimal
    ecstatic = '.90'
    happy = '.75'
    warm = '.65'
    meh = '.50'
    cool = '.35'
    gloomy = '0.25'
    doomed = '0.00'

    payload = HashMap()
    payload.put('text','RT USERNAME: Pleased to confirm this story. We filed today in Delhi High Court. Had enough of his campaign of calumny. URL')
    payload.put('polarity', BigDecimal(0.4102732628007269641027326280072696))


#
# Processor script
#
sentiments = dict(
    (name.title(), float(eval(name))) for name in ['ecstatic', 'happy', 'warm', 'meh', 'cool', 'gloomy', 'doomed'])


def label_sentiment_score(payload):

    score = payload['polarity']

    if type(score) == BigDecimal :
        score = score.floatValue()

    sentiment='Gloomy'
    for (k, v) in sorted(sentiments.items(), key=lambda x: x[1]):
        if score > v:
            sentiment = k
    return json.dumps({'sentiment': sentiment})

result = label_sentiment_score(payload)