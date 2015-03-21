# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

url = 'http://mm.taobao.com/687471686.htm'

request = urllib2.Request(url)
response = urllib2.urlopen(request)
urlDoc = response.read().decode('gbk')
print urlDoc

