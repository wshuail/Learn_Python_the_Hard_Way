from urllib2 import Request, urlopen, HTTPError, URLError

req = Request('http://www.csdn.com/callmewhy')

try:
    response = urlopen(req)

except URLError, e:
    if hasattr(e, 'code'):
        print 'We failed to reach a server.'
        print 'Error code: ', e.code
        
    else hasattr(e, 'reason'):
        print 'The server could not fullfill the request.'
        print 'Error code: ', e.code
    
else:
    print 'We success !'
