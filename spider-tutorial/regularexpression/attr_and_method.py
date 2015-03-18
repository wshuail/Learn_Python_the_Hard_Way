# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
# match 'letters+space+letters+anything'
m = re.match(r'(\w+) (\w+)(?P<test>.*)', 'hello world !')

print 'Attributes'
print 'm.string: ', m.string
print 'm.re: ', m.re
print 'm.pos: ', m.pos
print 'm.endpos: ', m.endpos
print 'm.lastindex: ', m.lastindex
print '\n'
print 'Method'
print 'm.group(): ', m.group()
print 'm.group(1, 2): ', m.group()
print 'm.groups(): ', m.groups
print 'm.groupdict(): ', m.groupdict()
print 'm.start(2): ', m.start()
print 'm.end(2): ', m.end()
print 'm.span(2): ', m.span()
print r'm.expand(r\'\g \g\g\'): ', m.expand(r'\2 \1\3')




















