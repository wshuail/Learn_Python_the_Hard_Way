# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

url = 'http://www.baidu.com/'

Values = {'name': 'WHY',
    'location': 'SDU',
    'language': 'Python'}
    
data = urllib2.urlencode(values) #code the data
req = urllib2.Request(url,data) #send request
response = urllib2.urlopen(req) #receive response
the_page = response.read() #read the response
