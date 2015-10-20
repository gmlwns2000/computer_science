#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Hee Jun Lee on 2015-10-18.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.
"""

import sys
import os

while true:
        loot=int(input("loot: "))
        adder=int(input("adder: "))
        times=int(input("times: "))
        a=loot
        b=0
        while b<times:
        	b=b+1
        	a=a+adder
                print("["+str(b)+"/"+str(times)+"]"+"("+str(b/times*100)+"%) "+str(a))

