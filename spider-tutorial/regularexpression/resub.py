# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'(\w+)(\w+)')

s = 'I say, hello world !'

# replace patttern in s by r'\2 \1' 
print re.sub(pattern, r'\2 \1', s)

def function(m):
    print m.group(1).title() + ' ' + m.group(2).title()

# replace pattern in s by r'\2 \1'
print re.sub(pattern, function, s)

 
