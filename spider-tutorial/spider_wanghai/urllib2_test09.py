# /usr/bin/env python
# -*- coding: utf-8 -*-


from urllib2 import Request, urlopen, HTTPError, URLError

req = Request('http://www.csdn.com/callmewhy')

try:
    response = urlopen(req)

except URLError, e:
    if hasattr(e, 'code'):
        print 'We failed to reach a server.'
        print 'Error code: ', e.code
        
    elif hasattr(e, 'reason'):
        print 'The server could not fullfill the request.'
        print 'Error code: ', e.reason
    
else:
    print 'We success !'
