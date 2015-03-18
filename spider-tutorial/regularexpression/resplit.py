# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'\d+')

match = re.split(pattern, r'one1two2three3four4')

if match:
    print match
