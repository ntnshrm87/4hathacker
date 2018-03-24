#!/usr/bin/python

from __future__ import with_statement
from urlparse import urlparse

def get_domain(url):
	 # load tlds, ignore comments and empty lines:
    	 with open("effective_tld_names.dat.txt") as tld_file:
    	  	tlds = [line.strip() for line in tld_file if line[0] not in "/\n"]
	
    	 url_elements = urlparse(url)[1].split('.')
   	 # url_elements = ["abcde","co","uk"]

    	 for i in range(-len(url_elements), 0):
        	last_i_elements = url_elements[i:]
        #    	i=-3: ["abcde","co","uk"]
        #    	i=-2: ["co","uk"]
        #    	i=-1: ["uk"] etc

         candidate = ".".join(last_i_elements) # abcde.co.uk, co.uk, uk
         wildcard_candidate = ".".join(["*"] + last_i_elements[1:]) # *.co.uk, *.uk, *
         exception_candidate = "!" + candidate

        # match tlds: 
         if (exception_candidate in tlds):
            return ".".join(url_elements[i:]) 
         if (candidate in tlds or wildcard_candidate in tlds):
            return ".".join(url_elements[i-1:])
            # returns "abcde.co.uk"

	 raise ValueError("Domain not in global list of TLDs")

#print get_domain("http://www.youtube.com")

