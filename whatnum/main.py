#what num
#main.py

import random
import time
import os

global gameon
gameon = True

def say(user,msg):
	print("["+time.strftime("%H:%M:%S",time.localtime())+"]"+" ("+user+") "+msg)
	if user=="Computer":
		try:
			os.system("say "+msg+"\n")
		except:
			pass

def gameStart():
	tryTimes=1
	targetNum=random.randint(0,10000)
	say("Computer","Okay, Player...")
	say("Computer","I will chose one number what I want!")
	say("Computer","Guess What!~")
	say("Computer","Ready...")
	for i in range(1,4):
		say("Computer",""+str(i))
		time.sleep(0.3)
	startTime=time.time()
	clear=False
	while not(clear):
		say("Computer","Lets GUESS! ")
		try:
			inp=input("["+str(tryTimes)+"th Try!] >U>S>E>R> ")
			if inp=="show me the money":
				say("System",str(targetNum))
			if inp=="":
				continue
			inp=int(inp)
			say("Me","Umm... "+str(inp)+"!")
		except:
			say("Computer","Ummm... I think it is not Number!")
			continue
		if inp>targetNum:
			say("Computer","I think less then you said...")
		elif inp<targetNum:
			say("Computer","I think more then you said...")
		elif inp==targetNum:
			case=random.randint(1,6)
			if case==1:
				say("Computer","Oh You are Correct! Wonderful!")
			elif case==2:
				say("Computer","Okay, I am Lose")
			elif case==3:
				say("Computer","LOL! You are Genius!")
			elif case==4:
				say("Computer","WOW! You are right!~ Congraturation!")
			elif case==5:
				say("Computer","HaHa! You Win!!")
			else:
				say("System","Oh... Something Gonna be wrong...<BUG#AVEW>")
				say("System","Debug Data: "+str(case))
			endTime=time.time()
			say("Computer",time.strftime("You Take %M minutes and %S seconds to Get Correct.",time.gmtime(endTime-startTime)))
			if tryTimes<5:
				say("Computer","And You do just "+str(tryTimes)+" times to Get Correct Answer!")
				say("Computer","I cant believe it!")
			else:
				say("Computer","And You do "+str(tryTimes)+" times to Get Correct Answer!")
			say("Computer","Lets Do This again!")
			clear=True
		else:
			say("System","Oh... Something Gonna be wrong...<BUG#GEDB>")
		if not(clear):
			tryTimes+=1

while gameon:
	print("=====================================")
	print("=  W E L L C O M E T O G U E S S !  =")
	print("=====================================")
	try:
		inp=str(input("Do you want Start? <Y:Yes> <N:No>: "))
	except:
		say("System","Please run game in Python3")
		exit()
	if inp=="n" or inp=="N":
		exit()
	elif inp.lower()=="y":
		gameStart()
	else:
		continue