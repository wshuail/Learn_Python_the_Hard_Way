# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

values = {'username': 'nawusicaa@foxmail.com', 'password': 'a13733752839'}
data = urllib.urlencode(values)

headers = {user_agent :'Mozilla/5.0 (X11; Linux x86_64)',
        'Referer': 'https://www.quora.com/'}

quora_url = 'http://www.quora.com'
request = urllib2.Request(quora_url, data, 10)

try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e. reason):
        print e.reason
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason')
        print e.reason
else:
    print 'OK!'

print response.read()
