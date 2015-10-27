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

debug=True

def Set(debug_mode)
    if debug_mode:
        debug=False
    else:
        debug=True
def Log(msg):
    if(debug):
        print("["+strftime("%B %dth %A %I:%M", localtime())+"] "+msg)
        time.sleep(0.5)
