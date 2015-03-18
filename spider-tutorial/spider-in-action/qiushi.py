# !/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2

page = 1
initial_url = 'http://www.qiushibaike.com/hot/page/'
url = initial_url + str(page)

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0)' }

try:
    request = urllib2.Request(url, headers = header)
    response = urllib2.urlopen(request)
    print response.read()
    
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print 'e.code: ' + e.code
    if hasattr(e, 'reason'):
        print 'e.reason: ', e.reason
    
