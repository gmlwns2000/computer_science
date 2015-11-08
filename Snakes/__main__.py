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
import threading

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

Debug.Set(True)

global draw_pause_length
draw_pause_length=0
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
global game_status
game_status=1
global game_drawing
game_drawing=False
global buf_scr
buf_scr=[]
global keyinput
keyinput=""
global keydown
keydown=False
global build_num
global nowframe
nowframe=0

Debug.Log("Update Buildnum...")

try:
    f=open("./.buildnum","r")
    build_num=int(f.read())
    build_num+=1
    f.close()
    f=open("./.buildnum","w")
    f.write(str(build_num))
    f.close()
    Debug.Log("Loaded Build Number")
except:
    Debug.Log("Can't Find Build Numberfile")
    fd=open("./.buildnum","w")
    build_num=1
    fd.write(str(build_num))
    fd.close()
    Debug.Log("Successed Make Build Number File!")

Debug.Log("Start Define Functions...")


def room_goto(room_id):
    global room
    room=room_id

def scr_draw(buf_scr, width, height):
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

def draw_pause(length):
    global draw_pause_length
    draw_pause_length+=length

def scr_clear(width, height):
    global buf_scr
    line=0
    while line<height:
        pos=0
        temp_line=[]
        while pos<width:
            temp_line.append(" ")
            pos=pos+1
        try:
            buf_scr[line]=temp_line
        except:
            buf_scr.append(temp_line)
        line=line+1

def read_key():
    global room
    global room_main
    global room_game
    global game_continue
    global keyinput
    global game_drawing
    keyinput="1"
    while True:
        if game_drawing==False:
            if room==room_game:
                keyinput=Console.Read()

def Debuger():
    global keyinput
    global keydown
    global game_drawing
    global game_status
    global room
    global build_num
    global draw_pause_length
    global nowframe
    global snake_x
    global snake_y
    global direction
    
    Debug.Log("Debuger: Build: #"+str(build_num))
    Debug.Log("Debuger: room: "+str(room))
    Debug.Log("Debuger: nowframe: "+str(nowframe))
    Debug.Log("Debuger: draw_pause_length: "+str(draw_pause_length))
    Debug.Log("Debuger: game_drawing: "+str(game_drawing))
    Debug.Log("Debuger: game_status: "+str(game_status))
    Debug.Log("Debuger: keyinput: "+str(keyinput))
    Debug.Log("Debuger: keydown: "+str(keydown))
    Debug.Log("Debuger: snake_x: "+str(snake_x))
    Debug.Log("Debuger: snake_y: "+str(snake_y))
    Debug.Log("Debuger: direction: "+str(direction))

def room1():
    global room
    global keyinput
    while (room == 1):
        Debug.Log("Title: Main Room")
        Debuger()
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
                time.sleep(0)
            elif inp=="n":
                cls()
                scr_clear(28,12)
                print("exit")
                exit()
        except:
            cls()
            continue

global snake_x
global snake_y
global direction
snake_x=16
snake_y=6
direction=4

def snake_update():
    global snake_x
    global snake_y
    global direction

def room2():
    #STEP
    global buf_scr
    global game_status
    global game_drawing
    global keyinput
    global draw_pause_length
    global nowframe
    global snake_x
    global snake_y
    global direction
    
    if game_status==1:
        draw_font(6,5,"press Space key")
        draw_font(9,6,"To start")
        if keyinput==" ":
            scr_clear(28,12)
            game_status=2
            draw_font(11,5,"Ready...")
            draw_font(12,6,"#####")
            snake_x=16
            snake_y=6
            direction=4
            draw_font(20,10,"*")
            keyinput=""
            draw_pause(1)
    elif game_status==3:
        if keyinput=="w":
            direction=1
            keyinput=""
        elif keyinput=="a":
            direction=2
            keyinput=""
        elif keyinput=="s":
            direction=3
            keyinput=""
        elif keyinput=="d":
            direction=4
            keyinput=""
        snake_update()
    time.sleep(0.1)
    #DRAW
    game_drawing=True
    cls()
    Debug.Log("Title: Main Room")
    Debuger()
    scr_draw(buf_scr, 28, 12)
    time.sleep(draw_pause_length)
    game_drawing=False
    #After Draw
    draw_pause_length=0
    nowframe+=1
    if game_status==2:
        game_status=3

Debug.Log("End Define Functions...")

def main():
    global room
    global room_main
    global room_game
    if room==room_main:
        room1()
    elif room==room_game:
        room2()

Debug.Log("Start Main Loop...")

while True:
    main()
