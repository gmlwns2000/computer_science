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
	skip=True
	while skip:
		try:
			vil=str(input("Select Village >>>"))
			if vil in data:
				skip=False
			else:
				print("There is no villages that have same name... Do you want Add Village???")
				ret=input("Y:yes, N:no >>>")
				if ret=="y" or ret=="Y":
					Add_Village(vil)
					skip=False
				else:
					print("then.. Select EXACT Village...")
		except:
			print("Oh.. User PLZ Enter EXACT Village... What is it that????")
	skip=True
	while skip:
		try:
			username=str(input("Input Username >>>"))
			if username in data[vil]:
				print("That user is already exist.")
				skip=False
			else:
				data[vil][username]=list()
				skip=False
		except:
			print("Oh.. User PLZ Enter EXACT Name... What is it that????")

def Give_Sheep():
	global data
	skip = True
	while skip:
		vilnames=list(data.keys())
		output=""
		for i in range(0,len(vilnames)):
			output+=" ("+str(i)+". "+vilnames[i]+") "
		print("Villages: "+output)
		try:
			ret=int(input("Select Number >>> "))
		except:
			skip=True
			continue
		if not(ret in range(0,len(vilnames))):
			continue
		print("Village Selected: "+vilnames[ret])

		vildata=dict(data[vilnames[ret]])
		usernames=list(vildata.keys())

		output=""
		for i in range(0,len(usernames)):
			output+=" ("+str(i)+". "+usernames[i]+") "
		print("Users: "+output)
		try:
			ret2=int(input("Select Number >>> "))
		except:
			continue
		print("User Selected: "+usernames[ret2])
		data[vilnames[ret]][usernames[ret2]].append(Make_Sheep())
		skip=False
			


while True:
	try:
		print("========== Welcome to Sheep Management System ==========")
		print("1: Add Village 2: Add User 3: Give Sheep 0: Show Database")
		ret = int(input(">>> "))
		if ret==0:
			print(data)
		elif ret==1:
			Add_Village(str(input("Type Vilname >>> ")))
		elif ret==2:
			Add_User()
		elif ret==3:
			Give_Sheep()
	except:
		pass
#END