# !/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://www.baidu.com'
req = Request(old_url)
response = urlopen(req)

print 'Info: ', response.info() # how info is used.
