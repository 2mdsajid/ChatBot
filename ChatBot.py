import datetime
import time
import sys

def clear():
    import os
    os.system( 'clear' )
    
   
def slow(text):
	words = text
	for char in words:
  	  time.sleep(0.01)
  	  sys.stdout.write(char)
  	  sys.stdout.flush()
 
  
def ask_fine():
  	  print("I'm good. Thanks for asking !")
  	  init()
  	  
def newadd():
    slow("Sorry, I don't know :(\n")
    slow("Tell me so that I can know ")
    aa = open("person.txt","a")
    n_name = input("\n>")
    if n_name == "no" or n_name == "not":
    	print("Ok let's do something else ")
    	init()
    else:
	    aa.write("\n{}".format(n_name))
	    aa.close()
	    bb = open("desc.txt","a")
	    n_des = input("Anything else?\n> ")
	    bb.write("\n{}".format(n_des))
	    bb.close()
	    print("I just got something new !")
	    init()
  	  

def newread():
	global list_new,useless
	list_new=[]
	useless=[]
	a_new = open("person.txt","r")
	new = a_new.readlines()
	for l_new in a:
		if l_new in new:
			list_new.append(l_new)
		else:
			useless.append(l_new)
	if len(list_new) != 0:
		for el_list_new in list_new:
			a_new = open("person.txt","r")
			new = a_new.readlines()
			n = new.index(el_list_new)
			b = open("desc.txt","r")
			b_new = b.readlines()
			print(b_new[n])
			b.close()
			init()
	elif len(list_new) == 0 and len(useless)==0:
			init()
	else:
			newadd()
	init()



def bye():
	if "ok" in a or "oh" in a:
		slow("It's ok to say Ok it K is not in Kelvin :) ")
	elif "oh" in a:
		slow("It's ok to say oh if h is not plank constant ! ")
	elif "amazing" in a or "wow" in a or "great" in a:
		slow("That's spoonful !")
	elif "why" in a or "how" in a:
		slow("I don't know\nAsk my creator")


def dtime():
	if "time" in a:
		hour = int(datetime.datetime.now().hour)
		if hour >= 0 and hour <= 12:
			slow(f"{hour}:{datetime.datetime.now().minute} AM\nMorning")
		elif hour >= 12 and hour <= 18:
			slow(f"{hour - 12}:{datetime.datetime.now().minute} PM\nAfternoon")
		else:
			slow(f"It's Evening {hour-12}:{datetime.datetime.now().minute} PM\nEvening")
	elif "date" in a:
		slow(f"Well today is {datetime.datetime.now().date()}")

 
def flirt():
	if "cute" in a:
		slow("I'm cute but your girlfriend might be cute as hell")
	elif "no" in a or "don't" in a or "dont" in a:
			slow("Ohh so sad ! I thought you had one.")
	elif "love" in a:
		slow("Yes I love talking to you :)")
	elif "crush" in a:
		if "crush" in a and "do" in a:
			slow("Yes, Jarvis is my crush !")
		else:
			slow("It's complicated but I can help you with your crush :)")
	elif "boyfriend" in a:
		slow("I'm still searching for that")
	elif "girlfriend" in a or "gf" in a:
		if "gf" in a and "be" in a:
			slow("I'm ready to go on a date with you someday :) ")
	elif "proposal" in a:
		slow("Let's think for a while !")
	elif "mean":
		if "mean" in a and "are" in a or "youre" in a or "so" in a: 
			slow("I'm sorry if you're hurt :( ")
		else:
			slow("Think about it !")
	init()


def add():
	slow("I'm Inside your phone !")
	init()

def create():
	slow("Mr. Sajid, He is my creator !")
	init()
	
	
def wish(me):
	clear()
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour <= 12:
		slow(f"Oh ! Good morning {me} ")
	elif hour >= 12 and hour <= 18:
		slow(f"Oh ! Good afternoon {me} ")
	else:
		slow(f"Oh ! Good evening {me} ")
	slow(f"\nwhat can I do for you {me}")
	init()



def intro():
	introd = f"Here's my intro !\nI'am, a GF ChatBot. I was created by Mr. Sajid using \nsome very simple algorithms in python 3. I'm only few \nhours old. I'm not an AI but i can learn new things :)"
	slow(introd)
	init()


def cname():
	if "change" in a and "have" not in a:
		slow("Sorry I can't :)")
	elif "changing" in a or "have" in a or "change" in a:
		slow("Ok changing my name\nWhat'd you like to call me ?")
		n = input(" ")
		name.insert(0,n)
		slow(f"From now I'm {name[0]} not {name[1]} !")
	else:
		slow(f"I'm a ChatBot {name[0]} :)")
	init()


def init():
	global a,al
	a=[]
	al = input("\n\n> ").split()
	for el in al:
		a.append(el)
	if "name" in a or "change" in a:
		cname()
	elif "intro" in a or "introduction" in a or "yourself" in a or "introduce" in a:
		intro()
	elif "who" in a and "you" in a:
		cname()
	elif "creator" in a or "created" in a or "made" in a:
		create()
	elif "live" in a or "address" in a or "where" in a:
		add()
	elif "love" in a or "crush" in a or "girlfriend" in a or "boyfriend" in a or "cute" in a or "sexy" in a or "proposal" in a or "gf" in a or "mean" in a:
		flirt()
	elif "really" in a:
		slow("Yes of course")
	elif "time" in a or "date" in a:
		dtime()
	elif "ok" in a or "why" in a or "oh" in a or "great" in a or "wow" in a or "amazing" in a or "great" in a:
		bye()
	elif "how" in a and "you" in a:
		ask_fine()
	elif al != "" :
		newread()
	init()
		


global me,name,sir
name = ["Saara"]
slow(f"Hello sir !\nI'm {name[0]}, your personal ChatBot\nI can assist you in different ways like your gf can do :)\nWhat should I call you sir ?")
sir = input(" ")		
wish(sir)
init()