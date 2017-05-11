#!/usr/bin/env jython
'''
Parse a list of tweets, extract the text
'''
import json
import java.util.Arrays

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
	floats = [float(x) for x in payload.replace('[','').replace(']','').split()]
	return java.util.Arrays.asList(floats)

if __name__ == '__main__':
	with open('./list-of-tweets.txt', 'r') as tweets:
		payload=tweets.read().replace('\n', '')
	channel='input'	
result=locals()[channel](payload)
