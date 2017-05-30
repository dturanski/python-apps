import json
#
# For testing, the module is not __main__ at runtime
#
if __name__ == "__main__":

    def new_item(text, polarity):
        return json.dumps({'text':text,'polarity':polarity})

    ecstatic = '.90'
    happy = '.75'
    warm = '.65'
    meh = '.50'
    cool = '.35'
    gloomy = '0.25'
    doomed = '0.00'


    items = []
    items.append(new_item('some text',0.4102732628007269641027326280072696))
    items.append(new_item('some text', 0.2102732628007269641027326280072696))
    items.append(new_item('some text', 0))
    items.append(new_item('some text', 0.6102732628007269641027326280072696))
    items.append(new_item('some text', 0.9102732628007269641027326280072696))
    items.append(new_item('some text', 0.75))

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

if __name__ == "__main__":
    for item in items:
        print(label_sentiment_score(item))
else:
    result = label_sentiment_score(payload)