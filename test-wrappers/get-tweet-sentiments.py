#!/usr/bin/env python
'''
Parse a list of tweets, extract the text
'''
import json

def input(payload):
	tweets=json.loads(str(payload))
	text = []
	
	for tweet in tweets:
		if tweet['lang'] == 'en':
			val = tweet['text'].encode('ascii','ignore')
			text.append(val)

	return json.JSONEncoder().encode({"data": text })

def output(payload):
	return payload	

if __name__ == '__main__':
	with open('./list-of-tweets.txt', 'r') as tweets:
		payload=tweets.read().replace('\n', '')
	channel='input'	
	
result=locals()[channel](payload)
print(result)
