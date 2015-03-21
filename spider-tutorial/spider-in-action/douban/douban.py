# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Wang SL'
__description__ = '''this spider was used to scrape pictures on douban'''

import urllib
import urllib2
import re

# open the url and get the content of the page
douban_url = 'http://www.douban.com/photos/album/154371813/'
douban_request = urllib2.Request(douban_url)
douban_response = urllib2.urlopen(douban_request)
douban_doc = douban_response.read().decode('utf-8')

# get the url of the picture by regular expression
picture_pattern = re.compile('div class="photo_wrap">.*?<a href="(.*?)".*?class=', re.S)

picture_links = re.findall(picture_pattern, douban_doc)
if picture_links:
	for picture_link in picture_links:
		links = []
		links.append(picture_link)
else:
	print 'Failed to get the links !'


# open the links and download the pictures

for link in links:
	pic_request = urllib2.Request(link)
	pic_response = urllib2.urlopen(pic_request)
	pic_doc = pic_response.read().decode('utf-8')

	# get the url of the big picture
	big_pic_link_pattern = re.compile('<div class="image-show">.*?<img src="(.*?)/>', re.S)
	big_pic_link = re.search(big_pic_link_pattern, pic_doc)
	big_pic_doc = urllib2.urlopen(big_pic_link.group(1))
	big_pic_data = big_pic_doc.read()
	big_pic = open('figure', 'wb')
	big_pic.write(big_pic_data)
	print 'Saving the picture ...'
	big_pic.close()






