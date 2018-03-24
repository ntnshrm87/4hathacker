#!/usr/bin/python

import urllib2
import io

def get_robots_txt(url):
	if url.endswith('/'):
		path = url
	else:
		path = url + '/'

	request = urllib2.urlopen(path + 'robots.txt')
	return request.read().decode("utf-8")

#print get_robots_txt("http://www.youtube.com") 
