# !/usr/bin/env python
# -*- coding: utf-8 -*-

# tutorial of spider from Wanghai's blog

import urllib2
response = urllib2.urlopen ('http://www.baidu.com/')
html = response.read()
print html
