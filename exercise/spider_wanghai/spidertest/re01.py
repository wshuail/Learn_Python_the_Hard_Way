# -*- coding: utf-8 -*-
# a case about regular expression

import re
 
pattern = re.compile(r'hello')
 
match1 = pattern.match('hello world!')
match2 = pattern.match('helloo world!')
match3 = pattern.match('helllo world!')

if match1:
    print match1.group()
else:
    print 'match1 fail！'


if match2:
    print match2.group()
else:
    print 'match2 fail！'


if match3:
    print match3.group()
else:
    print 'match3 fail！'

