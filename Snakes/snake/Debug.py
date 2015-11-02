#!/usr/bin/env python
# encoding: utf-8
"""
__main__.py

Created by Hee Jun Lee on 2015-10-25.
Copyright (c) 2015 AinL. All rights reserved.
"""

import os
import time
from time import localtime, strftime

def Set(debug_mode):
    global debug
    if debug_mode:
        debug=True
    else:
        debug=False
def Log(msg):
    global debug
    if(debug):
        print("["+strftime("%B %dth %A %I:%M", localtime())+"] "+msg)
