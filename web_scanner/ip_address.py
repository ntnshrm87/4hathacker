#!/usr/bin/python
import os

def get_ip_address(url):
	command = "host " + url
	process = os.popen(command)
	results = str(process.read())
	marker = results.find("has address")+12
	y = results[marker:].splitlines()[0]
	return y

#print get_ip_address("http://www.4hathacker.in")
