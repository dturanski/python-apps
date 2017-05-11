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

	result = json.JSONEncoder().encode({"data": text })
	print(result)
	return result

def output(payload):
	return payload	

if __name__ == '__main__':
	with open('./list-of-tweets.txt', 'r') as tweets:
		payload=tweets.read().replace('\n', '')
	channel='input'	
headers['Content-Type']='application/json'	
result=locals()[channel](payload)
