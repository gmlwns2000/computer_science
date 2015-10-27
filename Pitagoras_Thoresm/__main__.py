#!/usr/bin/env python
# encoding: utf-8
"""
__main__.py

Created by Hee Jun Lee on 2015-10-26.
Copyright (c) 2015
"""

import sys
import os
import math

while True:
    try:
        w=float(input("width: "))
        h=float(input("height: "))
        outdis=math.sqrt(float(w)*float(w)+float(h)*float(h))
    except:
        print("==================================")
        continue
    print("result: "+str(outdis))
    print("==================================")
