# !/usr/bin/env python
# -*-coding: utf-8 -*-

__author__ = 'SL Wang'

# import re module (regula expression)
import re

# create compile object

pattern = re.compile(r'hello')

result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo SL Wang !')
result3 = re.match(pattern, 'helo SL Wang!')
result4 = re.match(pattern, 'hello SL Wang')

# check if success
if result1:
    print result1.group()
else:
    print 'result1 failed to match !'
    
if result2:
    print result2.group()
else:
    print 'result2 failed to match !'
    
if result3:
    print result3.group()
else:
    print 'result3 failed to match !'
    
if result4:
    print result4.group()
else:
    print 'result4 failed to match !'
    
    
