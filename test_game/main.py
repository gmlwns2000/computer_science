#programming game test
#BatNum

#imports
import time
import random

#global var
global gameon
gameon=True

#SCRIPS
global i_will_pick
i_will_pick=["I will pick a 3-digit number... Can you guess it?","I will Pick own number, and it is a 3-digit number!"]
global do_this
do_this=["Go!","Guess what~","You still wrong.. haha","Lets try!","Guess what!"]
global cant_understand
cant_understand=["It is not digits..."]
global wrong_len
wrong_len=["Hey player, I said... I think 3 digits NUMBER!"]
global you_correct
you_correct=["You Right!","Congraturation!"]


def say(usr, msg):		#it will support TTS on make through say msg cmd.
	print("["+time.strftime("%M:%S",time.localtime())+"] "+"("+usr+") "+msg)

def getScript(scrList):	#pick script randomly
	if len(scrList)==0:
		return ""
	else:
		return scrList[random.randint(0,len(scrList)-1)]

def check(targetNum,cmd):			#1->clear -1->Buged
	global wrong_len
	if len(cmd)==1:
		cmd="00"+cmd
	elif len(cmd)==2:
		cmd="0"+cmd
	elif len(cmd)==3:
		pass
	else:
		say("Computer",getScript(wrong_len))
		return -1
	resultMsg=""
	score=0
	for i in range(0,len(cmd)):
		if cmd[i]==targetNum[i]:
			if score==0:
				resultMsg+="FERMI"
				score+=2
			else:
				resultMsg+=", FERMI"
				score+=2
		else:
			for ii in range(0,len(cmd)):
				if cmd[i]==targetNum[ii]:
					if score==0:
						resultMsg+="PICO"
						score+=1
						ii=len(cmd)+10
					else:
						resultMsg+=", PICO"
						score+=1
						ii=len(cmd)+10
	if score==0:
		resultMsg+="BAGELS"
	elif score==6:
		return 1
	say("Computer",resultMsg)


def game():				#game loop
	global i_will_pick
	global do_this
	global cant_understand
	global you_correct

	startTime=time.time()
	clear=False
	targetNum=str(random.randint(0,999))
	tryTimes=1
	# make 3 digits
	if len(targetNum)==1:
		targetNum="00"+targetNum
	elif len(targetNum)==2:
		targetNum="0"+targetNum
	else:
		pass
	print("targetNum+"+targetNum)
	say("Computer",getScript(i_will_pick))
	while not(clear):
		#try:
		if tryTimes>20:		# check player faild
			say("Computer","You Faild!")
			clear=True
			break
		say("Computer",getScript(do_this))
		inp=input("Try "+str(tryTimes)+" Times >U>S>E>R> ")
		if inp=="show me the money":
			say("System","Cheat Result : "+str(targetNum))
		checkResult=check(targetNum,inp)
		if checkResult==1:
			say("Computer",getScript(you_correct))
			clear=True
			endTime=time.time()
			say("Computer","You take "+str(tryTimes)+" Times and "+str(int(endTime-startTime))+" Seconds.")
			break
		tryTimes+=1

while gameon:			#main loop
	print("===============================")
	print("=        S T A R T ?          =")
	print("===============================")
	say("System","Do You Want To Start? (Y:Yes, N:No)")
	try:
		inp = input(">U>S>E>R> ")
	except:
		say("System","Check your python version. This game need python3.x~")
		exit()
	if inp.lower()=="y":
		game()
	elif inp.lower()=="n":
		exit()
	else:
		print("Wrong input: "+inp.lower())