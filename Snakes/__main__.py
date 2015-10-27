#!/usr/bin/env python
# encoding: utf-8
"""
__main__.py

Created by Hee Jun Lee on 2015-10-25.
Copyright (c) 2015 AinL. All rights reserved.
"""

import os
import time
from snake import Debug

Debug.Set(True)

global room
room=1

global room_main
room_main=1
global room_game
room_game=2
global room_died
room_died=3
global room_score
room_score=4

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def room_goto(room_id):
    global room
    room=room_id

def room1():
    global room
    while (room == 1):
        cls()
        Debug.Log("Title: Main Room")
        print("==============================")
        print("=                            =")
        print("=                            =")
        print("=                            =")
        print("=                            =")
        print("=      ~ S N A K E S ~       =")
        print("=                            =")
        print("=                            =")
        print("=     ┌─┐          ┌─┐       =")
        print("=     │y│          │n│       =")
        print("=     └─┘          └─┘       =")
        print("=  continue        exit      =")
        print("=                            =")
        print("==============================")
        y="y"
        n="n"
        inp=str(input("CMD>"))
        Debug.Log("input: "+inp)
        try:
            if inp=="y":
                room_goto(room_game)
                Debug.Log("goto game : "+str(room))
                time.sleep(2)
            elif inp=="n":
                cls()
                scr_clear(28,12)
                print("exit")
                time.sleep(2)
                exit()
        except:
            continue

global buf_scr
buf_scr=[]

def scr_draw(buf_scr, width, height):
    print("==============================")
    line=0
    while line<height:
        line_str="="
        pos=0
        while pos<width:
            line_str=line_str+buf_scr[line][pos]
        line_str=line_str+"="
        print(line_str)
        line=line+1
    print("==============================")    

def scr_clear(width, height):
    global buf_scr
    line=0
    while line<height:
        pos=0
        
        while pos<width:
            buf_scr[line][pos]=" "
            pos=pos+1
        line=line+1

def room2():
    cls()
    scr_draw(buf_scr, 28, 12)
    print

def main():
    global room
    global room_main
    global room_game
    if room==room_main:
        room1()
    elif room==room_game:
        room2()

while True:
    main()
