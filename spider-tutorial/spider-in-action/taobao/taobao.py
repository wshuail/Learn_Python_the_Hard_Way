# -*- coding: utf-8 -*-

import base64
import urllib
import urllib2
import re

baseurl = 'http://mm.taobao.com/json/request_top_list.htm'

url = baseurl + '?page=' + str(1)
request = urllib2.Request(url)
response = urllib2.urlopen(request)
pageDoc = response.read().decode('gbk')

pattern = re.compile('<div class="list-item".*?<div class=".*?<a href="(.*?)".*?target.*?class=".*?>.*?<img.*?src="(.*?)".*?alt=".*?width=".*?>.*?</a>.*?</div>.*?<p class=".*?">.*?<a class=".*?".*?href=".*?target=".*?">(.*?)</a>.*?<em><strong>(.*?)</strong>.*?<span>(.*?)</span>.*?<span class=', re.S)
items = re.findall(pattern, pageDoc)
if items:
	for item in items:
		pagecontents = []
		pagecontents.append([item[0], item[1], item[2], item[3], item[4]])
#	return pagecontents
else:
	print 'Failed to get content.'

# mmrequest = urllib2.Request(infourl)
# mmresponse = urllib2.urlopen(mmrequest)
# mmDoc = mmresponse.read().decode('gkb')

# text introduction
introductionPattern = re.compile('</ul>.*?<p class="description">(.*?)</p>.*?<div class="', re.S)

# get the brief introduction of the taobao girls.
result = re.search(introductionPattern, pageDoc)
print result.group(1)


picLinkPattern = re.compile('div class="list-item">.*?<div class=".*?<a href="(.*?)".*?target=".*?>', re.S)
# get all pictures links
picLink = re.search(picLinkPattern, pageDoc)
print picLink.group(1)

# get pictures
picRequest = urllib2.Request(picLink.group(1))
picResponse = urllib2.urlopen(picRequest)
picDoc = picResponse.read().decode('gbk')
patternImg = re.compile('<img style=".*?src="(.*?)"/>', re.S)
picture_urls = re.findall(patternImg, picDoc)

for picture_url in picture_urls:
	u = urllib2.urlopen(picture_url)
	data = u.read()
	if data:
		data = base64.b64encode(data)
		f = open(data, 'rb')
		f.write(data)
		print 'Saving picture.'
		f.close()
	else:
		print 'Load pictures failed.'
	














