# !/usr/bin/env python
# -*- coding: utf-8 -*-i

import urllib
import urllib2
import urlparse

data = {}
data['word'] = 'Jecvay Notes'

data = urllib.urlencode(data)

url_values = urlparse.urlparse(data)

url = 'http://www.baidu.com/s?'

full_url = url + str(url_values)

request = urllib2.Request(full_url)
response = urllib2.urlopen(request)
data = response.read()

print data














