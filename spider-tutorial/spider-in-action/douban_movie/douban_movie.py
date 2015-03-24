# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Wang SL'
__description__ = '''this spider was used to scrape pictures on douban'''

import urllib
import urllib2
import re
import os

header = {'User_Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}

# open the url and get the content of the page
douban_url = 'http://movie.douban.com/subject/1889243/reviews'
douban_request = urllib2.Request(douban_url, headers = header)
douban_response = urllib2.urlopen(douban_request)
douban_doc = douban_response.read().decode('utf-8')

# get the url of the review links by regular expression
movie_link_pattern = re.compile('div class="review">.*?<div class="review-hd">.*?<a id=".*?rel=".*?href="(.*?)".*?class=.*?style=".*?>', re.S)

movie_links = re.findall(movie_link_pattern, douban_doc)
if movie_links:
	links = []
	for movie_link in movie_links:
		links.append(movie_link)
else:
	print 'Failed to get the links !'


# open the links and download the pictures

for link in links:
	print link
	review_request = urllib2.Request(link)
	review_response = urllib2.urlopen(review_request)
	review_doc = review_response.read().decode('utf-8')

	# get the url of the big picture
	review_pattern = re.compile('<div class="article">.*?<div class="main-bd">.*?<div.*?<div property=.*?class="">(.*?)</div>.*?<div class="main-ft">', re.S)
	review_content = re.findall(review_pattern, review_doc)
	if review_content:
		for review in review_content:
			note = open('review.txt', 'a')
			note.write(review.encode('utf-8'))
			print 'Saving reviews...'
			note.close()	
	else:
		print 'Failed to get reviews.'
'''	big_pic_doc = urllib2.urlopen(big_pic_link.group(1))
	big_pic_data = big_pic_doc.read()
	big_pic = open('figure', 'wb')
	big_pic.write(big_pic_data)
	print 'Saving the picture ...'
	big_pic.close()
'''



