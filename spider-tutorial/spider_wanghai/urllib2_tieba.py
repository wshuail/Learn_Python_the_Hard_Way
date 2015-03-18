# *-* coding: utf - 8 -*-

import string, urllib2

# define you function

def zhihu(url, begin_page, end_page):
    for i in range (begin_page, end_page + 1):
        sName = string.zfill(i, 5), '.html'
        print 'Downloading', str(i), 'web page, and save it as', sName, '...'
        f = open(sName, 'w+')
        m = urllib2.urlopen(url + string(i)).read()
        f.write()
        f.close

my_answer = 'http://www.zhihu.com/question/28294294/answer/'

begin_page = 00000001

end_page = 00000100


baiduurl = str(raw_input(u'Please write down the page, and delete numbers after \'pn\'.\n'))

begin_page = int(raw_input(u'the initial page: \n'))

end_page = int)raw_input(u'the last page: \n')

baidu_tieba()
