# !/usr/bin/env python
# -*- coding:utf-8 -*-

import re

pattern = re.compile(r'\d+')

for m in re.finditer(pattern, r'one1two2three3four4'):
    print m.group()
