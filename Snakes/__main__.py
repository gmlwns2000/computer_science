#!/usr/bin/env python
# encoding: utf-8
"""
__main__.py

Created by Hee Jun Lee on 2015-10-25.
Copyright (c) 2015 AinL. All rights reserved.
"""

import os
import time

room=1

room_main=1
room_game=2
room_died=3
room_score=4

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def room_goto(room_id):
        room=room_id

def room1():
        while room == 1:
                cls()
                print("==============================")
                print("=                            =")
                print("=                            =")
                print("=                            =")
                print("=                            =")
                print("=      ~ S N A K E S ~       =")
                print("=                            =")
                print("=                            =")
                print("=     ┌─┐      ┌─┐     =")
                print("=     │ y│      │ n│     =")
                print("=     └─┘      └─┘     =")
                print("=    continue      exit      =")
                print("=                            =")
                print("==============================")
                inp = input()
                try:
                        if inp=="y":
                                room=2
                                print("goto game : "+str(room))
                                time.sleep(2)
                        elif inp=="n":
                                print("exit")
                                time.sleep(2)
                                exit()
                except:
                        continue

def room2():
        cls()
        print("hello")

def main():
        if room==room_main:
                room1()
        elif room==room_game:
                room2()

while True:
        main()
