from urllib2 import Request, urlopen, HTTPError, URLError

req = Request('http://www.csdn.com/callmewhy')

try:
    response = urlopen(req)
    
except HTTPError, e:
    print 'The server could not fullfill the request.'
    print 'Error code: ', e.code
    
except URLError, e:
    print 'We failed to reach a server.'
    print 'Error code: ', e.code
    
else:
    print 'We success !'
