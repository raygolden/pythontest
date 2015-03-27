#!/usr/bin/env python
import urllib
import urllib2

url = "http://localhost:8080/check_app?limit=500"
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
