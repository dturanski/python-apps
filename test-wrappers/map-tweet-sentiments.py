import json
#
# Processor script
#

def label_sentiment_score(payload):
    sentiments = dict(
        (name.title(), float(eval(name))) for name in ['ecstatic', 'happy', 'warm', 'meh', 'cool', 'gloomy', 'doomed'])
    sentiments = sorted(sentiments.items(), key=lambda x: x[1])

    data = json.loads(payload)

    score = data.get('polarity',-1)

    if score < 0:
        return json.dumps({'sentiment' : 'Unknown'})

    sentiment='Gloomy'
    for (k, v) in sentiments:
        if score >= v:
            sentiment = k
    return json.dumps({'sentiment': sentiment})

result = label_sentiment_score(payload)