#!/usr/bin/env python
# encoding: utf-8
"""
__main__.py

Created by Hee Jun Lee on 2015-10-25.
Copyright (c) 2015 AinL. All rights reserved.
"""

########################################################
#                       import
########################################################

import os
import time
import sys
from snake import Debug
from snake import Console
from snake import Getch
import random
import threading

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

Debug.Set(False)

########################################################
#                         var
########################################################

global engine_on
engine_on=True
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
global keyout
keyout=False
global keydown
keydown=False
global build_num
global nowframe
nowframe=0
global scr_width
scr_width=86
global scr_height
scr_height=24
global search_x
search_x=0
global search_y
search_y=0
global game_score
game_score=0
global game_freq
game_freq=0.06
global game_on
game_on=True
global snake_x
global snake_y
global direction
snake_x=17
snake_y=6
direction=4
global game_feeded
game_feeded=0
global game_highscore
game_highscore=0
global move_count
move_count=0

########################################################
#                       INIT
########################################################

try:
    scr_width = int(sys.argv[1])
    scr_height = int(sys.argv[2])
except:
    scr_width=76
    scr_height=21

if scr_width<30:
    scr_width=30
if scr_height<12:
    scr_height=12

Debug.Log("Update Buildnum...")

if Debug.debug:
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
else:
    f=open("./.buildnum","r")
    build_num=int(f.read())
    f.close()

Debug.Log("Start Define Functions...")

########################################################
#                   DRAW FUNCTION
########################################################

def draw_getpixel(x,y):
    global buf_scr
    try:
        return buf_scr[y][x]
    except:
        return " "

def draw_pixel(x,y,char):
    try:
        global buf_scr
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

########################################################
#                   SCREEN FUNCTION
########################################################

def scr_draw(buf_scr, width, height):
    global scr_width
    global scr_height
    cls()
    Console.Write(""+"="*(scr_width+2)+"\n")
    line=0
    while line<height:
        Console.Write("=")
        pos=0
        line_buf=buf_scr[line]
        while pos<width:
            Console.Write(line_buf[pos])
            pos=pos+1
        Console.Write("=\n")
        line=line+1
    Console.Write("="*(scr_width+2)+"\n")

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

########################################################
#                   DEBUGER FUNCTION
########################################################

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
    global search_x
    global search_y
    global direction
    global keyout
    
    Debug.Log("Debuger: Build: #"+str(build_num))
    Debug.Log("Debuger: room: "+str(room))
    Debug.Log("Debuger: nowframe: "+str(nowframe))
    Debug.Log("Debuger: draw_pause_length: "+str(draw_pause_length))
    Debug.Log("Debuger: game_drawing: "+str(game_drawing))
    Debug.Log("Debuger: game_status: "+str(game_status))
    Debug.Log("Debuger: keyinput: "+str(keyinput))
    Debug.Log("Debuger: keydown: "+str(keydown))
    Debug.Log("Debuger: keyout: "+str(keyout))
    Debug.Log("Debuger: snake_x: "+str(snake_x))
    Debug.Log("Debuger: snake_y: "+str(snake_y))
    Debug.Log("Debuger: search_x: "+str(search_x))
    Debug.Log("Debuger: search_y: "+str(search_y))
    Debug.Log("Debuger: direction: "+str(direction))

########################################################
#                   GAME FUNCTION
########################################################

def read_key():
    global room
    global room_main
    global room_game
    global game_continue
    global keyinput
    global game_drawing
    global game_on
    global keyout
    keyinput="1"
    keyout=False
    while game_on:
        if game_drawing==False:
            if room==room_game:
                keyinput=Console.Read()
    keyout=True

def game_exit():
    global game_on
    global engine_on
    game_on=False
    engine_on=False
    exit()

def game_stop_input():
    global thread_input
    global keyinput
    global game_on
    global keyout
    keyinput=""
    game_on=False
    print("Press Enter To Exit")
    while not(keyout):
        time.sleep(0.1)

def game_start_input():
    global thread_input
    global keyinput
    global game_on
    game_on=True
    thread_input = threading.Thread(target=read_key, args=())
    keyinput=""
    thread_input.start()

def game_load_high():
    global game_highscore
    try:
        f=open(".highscore","r")
        game_highscore=int(f.read())
        f.close()
    except:
        fd=open(".highscore","w")
        fd.write(str(game_highscore))
        fd.close()

def game_save_high(highscore):
    global game_highscore
    is_high=False
    if (highscore>game_highscore):
        f=open(".highscore","w")
        f.write(str(highscore))
        f.close()
        game_highscore=highscore
        is_high=True
    return is_high

def game_ev_snake_died():
    global game_score
    global scr_height
    global scr_width
    global game_status
    high_result=game_save_high(game_score)
    game_status=4
    scr_clear(scr_width,scr_height)
    draw_game_restartmsg(high_result)

def draw_game_restartmsg(result):
    global game_highscore
    draw_font(int(scr_width/2-5),int(scr_height/2)-1,"You LOOSE")
    draw_font(int(scr_width/2-9),int(scr_height/2),"press y to continue")
    draw_font(int(scr_width/2-7),int(scr_height/2)+1,"press n to exit")
    draw_font(int(scr_width/2-8),int(scr_height*0.67),"===HighScore===")
    draw_font(int(scr_width/2-int(len(str(game_highscore)+" points")/2)-1),int(scr_height*0.67)+1,str(game_highscore)+" points")
    if result:
        draw_font(int(scr_width/2-7),int(scr_height*0.67)+2,"NEW HIGHSCORE!")

def draw_game_ready():
    global snake_x
    global snake_y
    draw_font(int(scr_width*0.5)-4,int(scr_height*0.5)-3,"Ready...")
    draw_font(int(scr_width*0.5)-2,int(scr_height*0.5),"#####")
    draw_font(int(scr_width*0.83),int(scr_height*0.76),"*")
    snake_x=int(scr_width*0.5)+2
    snake_y=int(scr_height*0.5)

########################################################
#                   SNAKE FUNCTION
########################################################

def snake_tail():
    global snake_x
    global snake_y
    global search_x
    global search_y
    global game_status
    global scr_width
    global scr_height
    if not(draw_getpixel(snake_x,snake_y)=="#"):
        game_exit()
        return ""
    if draw_getpixel(snake_x+1,snake_y)=="#":
        search_x=snake_x+1
        search_y=snake_y
    elif draw_getpixel(snake_x-1,snake_y)=="#":
        search_x=snake_x-1
        search_y=snake_y
    elif draw_getpixel(snake_x,snake_y+1)=="#":
        search_x=snake_x
        search_y=snake_y+1
    elif draw_getpixel(snake_x,snake_y-1)=="#":
        search_x=snake_x
        search_y=snake_y-1
    pre_x=snake_x
    pre_y=snake_y
    find=True
    count=0
    while find:
        count+=1
        if count>scr_width*scr_height:
            game_ev_snake_died()
            return "oh"
        findd=True
        if draw_getpixel(search_x-1,search_y)=="#":
            if not(search_x-1==pre_x):
                findd=False
                pre_x=search_x
                search_x=search_x-1
                pre_y=search_y
                search_y=search_y
        if draw_getpixel(search_x+1,search_y)=="#":
            if not(search_x+1==pre_x):
                findd=False
                pre_x=search_x
                search_x=search_x+1
                pre_y=search_y
                search_y=search_y
        if draw_getpixel(search_x,search_y+1)=="#":
            if not(search_y+1==pre_y):
                findd=False
                pre_x=search_x
                search_x=search_x
                pre_y=search_y
                search_y=search_y+1
        if draw_getpixel(search_x,search_y-1)=="#":
            if not(search_y-1==pre_y):
                findd=False
                pre_x=search_x
                search_x=search_x
                pre_y=search_y
                search_y=search_y-1
        if findd:
            find=False
    draw_pixel(search_x,search_y," ")

def snake_feed():
    global scr_width
    global scr_height
    global game_score
    global game_feeded
    global move_count
    game_feeded+=1
    game_score+=int(100*(game_feeded+1.23)/(move_count+0.48))
    move_count=0
    feed_x=random.randint(2,scr_width-5)
    feed_y=random.randint(2,scr_height-5)
    feeded=True
    while feeded:
        if draw_getpixel(feed_x,feed_y)=="#":
            feed_x=random.randint(2,scr_width-5)
            feed_y=random.randint(2,scr_height-5)
        else:
            feeded=False
            draw_pixel(feed_x,feed_y,"*")

def snake_update():
    global snake_x
    global snake_y
    global scr_width
    global scr_height
    global direction
    global game_status
    global game_countinue
    global game_score
    if direction==1:
        if snake_y>0 and not(draw_getpixel(snake_x,snake_y-1)=="#"):
            snake_y-=1
            if draw_getpixel(snake_x,snake_y)=="*":
                draw_pixel(snake_x,snake_y,"#")
                snake_feed()
            else:
                draw_pixel(snake_x,snake_y,"#")
                snake_tail()
        else:
            game_ev_snake_died()
    elif direction==2:
        if snake_x>0 and not(draw_getpixel(snake_x-1,snake_y)=="#"):
            snake_x-=1
            if draw_getpixel(snake_x,snake_y)=="*":
                draw_pixel(snake_x,snake_y,"#")
                snake_feed()
            else:
                draw_pixel(snake_x,snake_y,"#")
                snake_tail()
        else:
            game_ev_snake_died()
    elif direction==3:
        if snake_y<scr_height-1 and not(draw_getpixel(snake_x,snake_y+1)=="#"):
            snake_y+=1
            if draw_getpixel(snake_x,snake_y)=="*":
                draw_pixel(snake_x,snake_y,"#")
                snake_feed()
            else:
                draw_pixel(snake_x,snake_y,"#")
                snake_tail()
        else:
            game_ev_snake_died()
    elif direction==4:
        if snake_x<scr_width-1 and not(draw_getpixel(snake_x+1,snake_y)=="#"):
            snake_x+=1
            if draw_getpixel(snake_x,snake_y)=="*":
                draw_pixel(snake_x,snake_y,"#")
                snake_feed()
            else:
                draw_pixel(snake_x,snake_y,"#")
                snake_tail()
        else:
            game_ev_snake_died()

########################################################
#                   ROOM FUNCTION
########################################################

def room_goto(room_id):
    global room
    room=room_id

def room1():
    global room
    global keyinput
    global scr_width
    global scr_height
    game_load_high()
    while (room == 1):
        scr_clear(scr_width,scr_height)
        draw_font(int(scr_width/2-7),int(scr_height/2.75),"~ S N A K E S ~")
        draw_font(int(scr_width/2-15),int(scr_height/2.75)+1,"Wellcome to Sanke World!")
        draw_font(int(scr_width/2-9),int(scr_height*0.75),"Enter y to Continue")
        draw_font(int(scr_width/2-8),int(scr_height*0.75)+1,"Enter n to Exit")
        scr_draw(buf_scr,scr_width,scr_height)
        Debug.Log("Title: Main Room")
        Debuger()
        y="y"
        n="n"
        inp=str(input("CMD>"))
        Debug.Log("input: "+inp)
        try:
            if inp=="y":
                room_goto(room_game)
                Debug.Log("goto game : "+str(room))
                scr_clear(scr_width,scr_height)
                game_start_input()
                cls()
            elif inp=="n":
                cls()
                scr_clear(scr_width,scr_height)
                game_exit()
        except:
            cls()
            continue

def room2():
    #STEP
    global room
    global room_main
    global buf_scr
    global game_status
    global game_drawing
    global game_freq
    global keyinput
    global draw_pause_length
    global nowframe
    global snake_x
    global snake_y
    global scr_width
    global scr_height
    global direction
    global game_score
    global game_feeded
    global move_count
    global scr_width
    global scr_height
    
    if game_status==1:
        draw_font(int(scr_width/2)-8,int(scr_height/2)-2,"Enter Space key")
        draw_font(int(scr_width/2)-4,int(scr_height/2)+2,"To start")
        draw_pause(0.5)
        if keyinput==" ":
            scr_clear(scr_width,scr_height)
            game_status=2
            direction=4
            keyinput=""
            draw_game_ready()
            draw_pause(1)
    elif game_status==3:
        if keyinput=="w":
            direction=1
            keyinput=""
            move_count+=1
        elif keyinput=="a":
            direction=2
            keyinput=""
            move_count+=1
        elif keyinput=="s":
            direction=3
            keyinput=""
            move_count+=1
        elif keyinput=="d":
            direction=4
            keyinput=""
            move_count+=1
        snake_update()
        if direction==1 or direction==3:
            draw_pause(game_freq)
    elif game_status==4:
        draw_pause(0.5)
        if keyinput=="n" or keyinput=="N":
            game_stop_input()
            game_status=1
            direction=4
            room_goto(room_main)
        elif keyinput=="y" or keyinput=="Y":
            scr_clear(scr_width,scr_height)
            game_status=2
            game_score=0
            game_feeded=0
            move_count=0
            direction=4
            keyinput=""
            draw_pause(1)
            draw_game_ready()
    #DRAW
    scr_draw(buf_scr, scr_width,scr_height)
    print("Score: "+str(game_score)+" points!")
    Debug.Log("Title: Main Room")
    Debuger()
    #After Draw
    time.sleep(game_freq+draw_pause_length)
    draw_pause_length=0
    nowframe+=1
    if game_status==2:
        game_status=3

Debug.Log("End Define Functions...")

def main():
    global room
    global room_main
    global room_game
    global scr_width
    global scr_height
    if room==room_main:
        room1()
    elif room==room_game:
        room2()

Debug.Log("Start Main Loop...")

while engine_on:
    main()