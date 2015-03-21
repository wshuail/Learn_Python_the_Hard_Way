# !/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

page = 1
initial_url = 'http://www.qiushibaike.com/hot/page/'
url = initial_url + str(page)

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0)' }

try:
    request = urllib2.Request(url, headers = header)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?</a>.*?<a.*?>(.*?)</a>.*?</div>.*?'+
    '<div.*?class="content".*?title="(.*?)">'+
                        '(.*?)</div>.*?<div.*?>' + 
                        '.*?<div.*?class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item[0], item[1], item[2], item[3]
#        print item[0], item[1], item[2], item[3], item[4]
                     
                     
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print 'e.code: ' + e.code
    if hasattr(e, 'reason'):
        print 'e.reason: ', e.reason                    
                     
                     
                     
                     
                     
                     
                     
                     
