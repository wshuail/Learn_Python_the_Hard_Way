import urllib
import urllib2

url = 'http://www.baidu.com/'

Values = {'name': 'WHY',
    'location': 'SDU',
    'language': 'Python'}
    
data = urllib2.urlencode(values) #编码工作
req = urllib2.Request(url,data) #发送请求，同时传data表单
response = urllib2.urlopen(req) #接收反馈信息
the_page = response.read() #读取反馈信息
