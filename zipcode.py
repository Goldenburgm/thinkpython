#!/usr/bin/python

import urllib

zipcode = "02492"

url = 'http://uszip.com/zip/' + zipcode
open_url = urllib.urlopen(url)

for line in open_url.fp:
	line = line.strip()
	if "Population" in line:
		print line
	if "Longitude" in line:
		print line	
	if "Latitude" in line:
		print line

open_url.close()			
		

