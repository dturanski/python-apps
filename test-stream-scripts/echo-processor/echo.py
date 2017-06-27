import sys
from springcloudstream.stream import Processor
__author__ = 'David Turanski'


def echo(data):
    return data


Processor(echo,sys.argv).start()