# -*- coding: utf-8 -*-
import urllib2

# creat a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# username and password
top_level_url = 'http://www.example.com/foo'

# if know realm, instead 'None'
password_mgr.add_password(None, top_level_url, 'why', 'abc123')

# creat a handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

#creat an opener
opener = urllib2.bulid_opener(handler)

a_url = 'http://www.baidu.com'

# open it by opener
opener.open(a_url)

#use opener
urllib2.install_opener(opener)
