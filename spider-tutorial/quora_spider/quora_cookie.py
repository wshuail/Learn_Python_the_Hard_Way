# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import cookielib

quora_url = 'http://www.quora.com'

# create a file to store cookie
filename = 'quora_cookie.txt'

# state a object to save cookie and write them into file.
cookie = cookielib.MozillaCookieJar(filename)

# state an object to save cookis
# cookie = cookielib.CookieJar() # this step has been insteaded.

# process the cookie
handler = urllib2.HTTPCookieProcessor(cookie)

# construct the opener by handler
opener = urllib2.build_opener(handler)

# steps below is no need
# response = opener.open(quora_url)
# for item in cookie:
#     print 'name: '+ item.name
#     print 'value: '+ item.value

# save cookie to the txt file
cookie.save(ignore_discard = True, ignore_expires = True)




















