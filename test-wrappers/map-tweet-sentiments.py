import json


def label_sentiment_score(payload):
    sentiments = dict(
        (name.title(), eval(name)) for name in ['ecstatic', 'happy', 'warm', 'meh', 'cool', 'gloomy', 'doomed'])
    doc = json.loads(payload)
    score = float(doc['polarity'])

    for (k, v) in sorted(sentiments.items(), key=lambda item: (item[1], item[0])):
        if score > v:
            sentiment = k
    return json.dumps({'sentiment': sentiment})


if __name__ == "__main__":
    ecstatic = .90
    happy = .75
    warm = .65
    meh = .50
    cool = .35
    gloomy = 0.25
    doomed = 0.00

    import sys

    payload = sys.stdin.readline()

result = label_sentiment_score(payload)

if __name__ == "__main__":
    print(result)
