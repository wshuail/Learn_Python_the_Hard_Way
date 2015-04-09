# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib

quora_url = 'https://www.zhihu.com/'

filename = 'quora_cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))


postdata = urllib.urlencode({'username':'',
                            'password': ''})
        
result = opener.open(quora_url, postdata)
                            
cookie.save(ignore_discard = True, ignore_expires = True)

print result.read()

