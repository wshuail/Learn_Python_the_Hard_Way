# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import gzip
import re
import cookielib
import urllib
import urllib2
import StringIO
import chardet

# decompress the web page
def decompress(data):
    if data.info().get('Content-Encoding') == 'gzip':
        buf = StringIO.StringIO(data.read())
        gzip_f = gzip.GzipFile(fileobj=buf)
        content = gzip_f.read()
    else:
        content = data.read()
    return content


# define the opener
def getOpener(head):
    # deal with the coockies
    cookies = cookielib.CookieJar()
    pro = urllib2.HTTPCookieProcessor(cookies)
    opener = urllib2.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
'''
header = {
    'Connection': 'Keep-Alive',
    'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.douban.com',
    'Referer': 'http://www.douban.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '90'
}
'''
header_2 = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'}


url = 'http://www.douban.com/accounts/login'
opener = getOpener(header_2)

id = ''
psword = ''
postdata = {
        'source': 'index_nav',
        'form_email': id,
        'form_password': psword,
        'remember': 'on'
        }
postData = urllib.urlencode(postdata)
response = opener.open(url, data = postData)
page = decompress(response)

print page
