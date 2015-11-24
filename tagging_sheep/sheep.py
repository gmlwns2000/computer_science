#moc.programing
#Tagging sheep
from string import ascii_lowercase
import random

global names
names=["LOL","Jhon","Josep","Lenchen","RailGun","Mikoto","Taeho","Hee","Jin","Lin","Chen","Briln","Alin","Mia","Ship","make","Sheep","Weh","Heeg","Lagg","Adventure","Tue","Mon","Sun","Moon","To The Moon","I AM YOUR FATHER!"]
global tags
tags=list(range(0,10000))
skip=True
global data
data=dict()

def Make_Sheep():
	global tags
	global names
	name=""
	ret =[]
	name=names[random.randint(0,len(names))]
	ret.append(name)
	tag=random.randint(0,len(tags)-1)
	ret.append(tags[tag])
	del tags[tag]
	return ret

def Add_Village(vilname):
	global data
	if not(vilname in data):
		data[vilname]=dict()

def Add_User():
	global data
	skip=true
	while skip:
		try:
			vil=str(input("Select Village >>>"))
			if vil in data:
				skip=False
			else:
				print("There is no villages that have same name... Do you want Add Village???")
				ret=input("Y:yes, N:no >>>")
				if ret=="y" or ret=="Y":
					skip=False
				else:
					print("then.. Select EXACT Village...")
		except:
			print("Oh.. User PLZ Enter EXACT Village... What is it that????")
	skip=true
	while skip:
		try:
			username=str(input("Input Username >>>"))
			if username in data[vil]:
				print("That user is already exist.")
				skip=False
			else:
				data[vil][username]=list()
		except:
			print("Oh.. User PLZ Enter EXACT Name... What is it that????")

def Give_Sheep():
	global data

while True:
	try:
		print("Welcome to Sheep Management System")
		print("1: Add Village 2: Add User 3: Give Sheep 0: Show Database")
		ret = int(input(">>>"))
		if ret==0:
			print(data)
		elif ret==1:
			ret=input("Type Vilname")
			Add_Village(str(ret))
		elif ret==2:
			Add_User()
		elif ret==3:
			pass
#END
#what??
