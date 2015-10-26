#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Hee Jun Lee on 2015-10-18.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

line=95

while True:
    start_time=time.time()
    loot=int(input("loot: "))
    adder=int(input("adder: "))
    times=int(input("times: "))
    a=loot
    b=0
    while b<times:
       	b=b+1
       	a=a+adder
       	cls()
        print("["+str(b)+"/"+str(times)+"]"+"("+str(float(b)/float(times)*100)+"%) Now Value: "+str(a))
        v=0
        progress_bar="["
        while v<=((float(b)/float(times))*line):
            progress_bar=progress_bar+"="
            v=v+1
        v=0
        while v<(line-((float(b)/float(times))*line)):
            progress_bar=progress_bar+"-"
            v=v+1
        print(progress_bar+"]")

    cls()
    print("===========================================================================")
    print("=                ===   =====   ====  =   =  =     =====                   =")
    print("=                =  =  =      =      =   =  =       =                     =")
    print("=                =   = =      =      =   =  =       =                     =")
    print("=                =  =  =====   ===   =   =  =       =                     =")
    print("=                ===   =          =  =   =  =       =                     =")
    print("=                =  =  =          =  =   =  =       =                     =")
    print("=                =   = =====  ====    ===   =====   =                     =")
    print("===========================================================================")
    print("")
    print("Result Value(loot+adder*times): "+str(a))
    print("Take Time(ms): "+str(int(time.time()*100)-int(start_time*100))+"ms")
    print("How long take per add: "+str(float(int(time.time()*100)-int(start_time*100))/times))
    print("")
    print("==========================E  N  D==========================================")
    input("Press ENTER!!!!!!!!!!!!!!!!!")
    cls()
