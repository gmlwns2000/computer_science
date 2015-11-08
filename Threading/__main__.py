#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Hee Jun Lee on 2015-10-25.
Copyright (c) 2015 AinL. All rights reserved.
"""

import os
import time
import threading

def main1():
    while True:
        print("2")

def main2():
    while True:
        print("1")

th = threading.Thread(target=main1, args=())
th.start()
th1 = threading.Thread(target=main2, args=())
th1.start()