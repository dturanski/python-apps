import json

def label_sentiment_score(payload):
    sentiments = dict(
        (name.title(), float(eval(name))) for name in ['ecstatic', 'happy', 'warm', 'meh', 'cool', 'gloomy', 'doomed'])

    score = float(payload['polarity'])

    sentiment='Gloomy'
    for (k, v) in sorted(sentiments.items(), key=lambda x: x[1]):
        if score > v:
            sentiment = k
    return json.dumps({'sentiment': sentiment})

#
# For testing, the module is not __main__ at runtime
#
if __name__ == "__main__":
    from java.util import HashMap
    ecstatic = '.90'
    happy = '.75'
    warm = '.65'
    meh = '.50'
    cool = '.35'
    gloomy = '0.25'
    doomed = '0.00'

    import sys

    payload = HashMap()
    payload.put('text','RT USERNAME: Pleased to confirm this story. We filed today in Delhi High Court. Had enough of his campaign of calumny. URL')
    payload.put('polarity', 0.87612610210917)

result = label_sentiment_score(payload)
