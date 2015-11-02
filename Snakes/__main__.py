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
from snake import Console
from snake import Getch
import threading as Thrd

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
                scr_clear(28,12)
                th = threading.Thread(target=read_key, args=())
                th.start()
                time.sleep(1)
            elif inp=="n":
                cls()
                scr_clear(28,12)
                print("exit")
                time.sleep(1)
                exit()
        except:
            continue

global buf_scr
buf_scr=[]

def scr_draw(buf_scr, width, height):
    cls()
    Debug.Log("Title: Game Room")
    print("==============================")
    line=0
    while line<height:
        Console.Write("=")
        pos=0
        line_buf=buf_scr[line]
        while pos<width:
            Console.Write(line_buf[pos])
            pos=pos+1
        print("=")
        line=line+1
    print("==============================")    

def draw_pixel(x,y,char):
    try:
         buf_scr[y][x]=char
    except:
        pass

def draw_font(x,y,msg):
    pos=0
    while pos<len(msg):
        try:
            buf_scr[y][x+pos]=msg[pos]
        except:
            pass
        pos+=1

def scr_clear(width, height):
    global buf_scr
    line=0
    while line<height:
        pos=0
        temp_line=[]
        while pos<width:
            temp_line.append(" ")
            pos=pos+1
        buf_scr.append(temp_line)
        line=line+1

global game_continue
global game_drawing
game_continue=False
game_drawing=False

def read_key():
    global room
    global room_main
    global room_game
    global game_continue
    while 1:
        if game_drawing==False:
            if room==room_game:
                keyinput=Getch._Getch
                if (keyinput=="s" or keyinput=="S"):
                    game_continue=True
                    scr_clear(28,12)

def room2():
    #STEP
    global buf_scr
    global game_continue
    #POST_DRAW
    game_drawing=True
    if game_continue==False:
        draw_font(6,5,"press Space key")
        draw_font(9,6,"To start")
    #elif game_continue==True:
    
    game_drawing=False
    time.sleep(0.1)
    #DRAW
    scr_draw(buf_scr, 28, 12)

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
