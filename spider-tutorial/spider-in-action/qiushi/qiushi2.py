# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Wang Shuailong'

import urllib
import urllib2
import re
import thread
import time

class QSBK(object):
    # define sone initial objects
    def __init__(self):
        self.initial_page = 1
        self.agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0)'
        self.header = {'User-Agent': self.agent}
        self.stories = []
        self.enable = False
        
    # Get page context
    def getPage(self, initial_page):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(self.initial_page)
            request = urllib2.Request(url, headers = self.header)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
            
            # set URLError
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print 'e.code: ', e.code
            if hasattr(e, 'reason'):
                print 'e.reason: ', e.reason
    
    # scrape context we want by re.
    def getPageItems(self, initial_page):
        # make the page exist.
        content = self.getPage(initial_page)
        if not content:
            print 'The page has not existed !'
            return None
        # set regular expression, which will return items we want
        pattern = re.compile('<div.*?class="author.*?</a>.*?<a.*?>(.*?)</a>.*?</div>.*?'+
                             '<div.*?class="content".*?title="(.*?)">'+
                             '(.*?)</div>.*?<div.*?>' + 
                             '.*?<div.*?class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, content)
        # save the items
        pageStories = []
        # append the items into the pageStories
        for item in items:
            pageStories.append([item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip()])
            return pageStories
            
    # load content on the new page
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) <= 2:
                pageStories = self.getPageItems(self.initial_page)
                
                if pageStories:
                    self.stories.append(pageStories)
                    self.initial_page = self.initial_page + 1
                    
    def getOneStory(self, pageStories, initial_page):
        for story in pageStories:
            input = raw_input('> ')
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return None
            print u'page: %d\tauthor: %s\tTime: %s\n%s\nVotes: %s\n' %(initial_page, story[0], story[1], story[2], story[3])
            
    # How to  start
    def start(self):
        print 'Loading pages from QiuShiBaiKe...'
        print 'If you want to see content, please hit ENTER. Or hit \'Q\'.'
        self.enable = True
        self.loadPage()
        nowpage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowpage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowpage)
             
spider = QSBK()
spider.start()           
                     
                     
                     
                     
                     
                     
                     
