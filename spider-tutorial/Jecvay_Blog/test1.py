# -*- coding: utf-8 -*-

import urllib
import urllib2

url = 'http://www.google.com.hk'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
response = response.read()

print response
