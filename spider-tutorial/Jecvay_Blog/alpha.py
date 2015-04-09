# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
from httplib import getheader
from collections import deque

queue = deque()
visited = set()  # an empty set to stored web pages which have beenn visited.

url = 'http://news.dbanotes.net'  # the initial page

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()  # The first element
    visited |= {url}  # marked as visited

    print 'Scrapped: ', str(cnt), '\t', 'Scrapping: ', url

    cnt += 1
    urlrequest = urllib2.Request(url)
    urlresponse = urllib2.urlopen(urlrequest, timeout = 3)
#    if 'html' not in urlresponse.getheader('Content-Type'):
#        continue

    # process Error
    try:
        data = urlresponse.read().decode('utf-8')
    except:
        continue

    # scrapy elements by regular expression, and judge if it hass been visited.
    linkre = re.compile('href="(.+?)"', re.S)
    links = re.findall(linkre, data)
    for x in links:
        if 'http' in x and x not in visited:
            queue.append(x)
            print 'add to query', x

