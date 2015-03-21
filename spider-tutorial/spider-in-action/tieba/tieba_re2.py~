# !/usr/bin/dev python
# -*- coding: utf-8 -*-

__author__ = 'Wang Shuailong'

import urllib
import urllib2
import re


    # remove 'img' tag
removeImg = re.compile('<img.*?>| {7}|')
    # remove link
removeAddr = re.compile('<a>*?>|</a>')
    # change next line to \n
replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # change table tag to \t
replaceTD = re.compile('<td>')
    # two space before paragraph
replacePara = re.compile('</p.*?>')
    #tags for changing lines
replaceBR = re.compile('<br><br>|<br>')
    # remove other tags
removeExtraTag = re.compile('<.*?>')
    
def replace(x):
    x = re.sub(removeImg, '', x)
    x = re.sub(removeAddr, '', x)
    x = re.sub(replaceLine, '', x)
    x = re.sub(replaceTD, '', x)
    x = re.sub(replacePara, '', x)
    x = re.sub(replaceBR, '', x)
    x = re.sub(removeExtraTag, '', x)
    return x.strip()

url = 'http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'

agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0)'
header = {'User-Agent': agent}

def getPageContent(url):
    try:
        request = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(request)
        pageContent = response.read()
        if pageContent:
            print 'Get the web page successfully.'
            return pageContent
        else:
            print 'Failed to get the web page.'

    except urllib2.URLError, e:
        if hasattr(e, code):
            print 'e.code: ', e.code
        if hasattr(e, reason):
            print 'e.reason: ', e.reason

def getPageNum():
    patternPageNum = re.compile('<span class="red".*?style="margin.*?</span>.*?<span.*?>(.*?)</span>', re.S)
    pageNum = re.search(patternPageNum, pageContent)
    if pageNum:
        print result.group(1).strip()
    else:
        print 'Failed to get the number of the page.'

def getTitle():
    patternTitle = re.compile('.*?<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
    title = re.search(patternTitle, pageContent)
    if title:
        print title.group(1).strip()
    else:
        print 'Failed to get the title.'

def getContent():
    patternContent = re.compile('.*?<cc><div id=".*?".*?class=".*?">(.*?)</div><br></cc><br><div class=".*?></div>', re.S)
    items = re.findall(patternContent, pageContent)
    contents = []
    for item in items:
        item = '\n'+replace(item)+'\n'
        contents.append(item.encode('utf-8'))
    return contents
    print contents
        
