# -*- coding: utf-8 -*-

import re

a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)

b = re.compile(r"\d+\.\d*")

match11 = a.match('3.1415')
match12 = a.match('33')
match21 = b.match('3.1415')
match22 = b.match('33') 

if match11:
    print match11.group()
else:
    print u'match11 is not a floar number'
    
if match12:
    print match12.group()
else:
    print u'match12 is not a floar number'
    
if match21:
    print match21.group()
else:
    print u'match21 is not a floar number'

if match22:
    print match22.group()
else:
    print u'match22 is not a floar number'
