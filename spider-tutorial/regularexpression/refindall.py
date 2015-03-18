# !/usr/bin/env pthon
# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'\d+')

match = re.findall(pattern, r'one1two2three3four4')

if match:
    print match
