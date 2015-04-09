# !/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

# the url below is shortened
old_url = 'http://t.cn/RAI54Qd' 

# When the url is opened, it will be different with the former one.
req = Request(old_url)
response = urlopen(req)

print 'Old url: '+ old_url
print 'Real url: ' + response.geturl() # how heturl is used.
