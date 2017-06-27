import sys
from datetime import datetime
from springcloudstream.stream import Processor

__author__ = 'David Turanski'

#06/01/16 09:45:11
def time_delta(data):
	format = '%m/%d/%y %H:%M:%S'
	delta = datetime.now() - datetime.strptime(data,format)
	return str(delta)


Processor(time_delta,sys.argv).start()