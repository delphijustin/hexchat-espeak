__module_name__ = "ESpeak"
__module_version__ = "0.1.0"
__module_description__ = "Espeak script for hexchat"

import hexchat # HexChat IRC interface
import subprocess
import random
import sys
import os
import time
import threading

DeleteMinutes = 15 #number of minutes after text file is created to delete it
TalkID = round(random.random()*100000,0)

def TalkTimer(fn):
	time.sleep(60*DeleteMinutes)
	os.remove(fn)
def MSGTalk(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		# strips the colours and the format
		word[i] = hexchat.strip(word[i], -1, 3)
	# in "word", the first part is the user who issued the message
	user = word[0]
	msg = word[1][0:]
	fn = "/tmp/.hcsay"+str(TalkID+random.random())
	myfile = open(fn,"w+")
	myfile.write(user+" says "+msg)
	myfile.close()
	timerThread=threading.Thread(target=TalkTimer, args=(fn,))
	timerThread.start()
	subprocess.Popen(["espeak","-f",fn])
	return hexchat.EAT_NONE
def ATalk(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		# strips the colours and the format
		word[i] = hexchat.strip(word[i], -1, 3)
	# in "word", the first part is the user who issued the message
	user = word[0]
	msg = word[1][0:]
	fn = "/tmp/.hcsay"+str(TalkID+random.random())
	myfile = open(fn,"w+")	
	myfile.write(user+" "+msg)
	myfile.close()
	timerThread=threading.Thread(target=TalkTimer, args=(fn,))
	timerThread.start()
	subprocess.Popen(["espeak","-f",fn])
	return hexchat.EAT_NONE
def JoinTalk(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		# strips the colours and the format
		word[i] = hexchat.strip(word[i], -1, 3)
	# in "word", the first part is the user who issued the message
	user = word[0]
	msg = word[1][0:]
	fn = "/tmp/.hcsay"+str(TalkID+random.random())
	myfile = open(fn,"w+")	
	myfile.write(user+" has joined "+msg)
	myfile.close()
	timerThread=threading.Thread(target=TalkTimer, args=(fn,))
	timerThread.start()
	subprocess.Popen(["espeak","-f",fn])
	return hexchat.EAT_NONE
def NickTalk(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		# strips the colours and the format
		word[i] = hexchat.strip(word[i], -1, 3)
	# in "word", the first part is the user who issued the message
	user = word[0]
	msg = word[1][0:]
	fn = "/tmp/.hcsay"+str(TalkID+random.random())
	myfile = open(fn,"w+")	
	myfile.write(user+" is now "+msg)
	myfile.close()
	timerThread=threading.Thread(target=TalkTimer, args=(fn,))
	timerThread.start()
	subprocess.Popen(["espeak","-f",fn])
	return hexchat.EAT_NONE
def PartTalk(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		# strips the colours and the format
		word[i] = hexchat.strip(word[i], -1, 3)
	# in "word", the first part is the user who issued the message
	user = word[0]
	msg = word[1][0:]
	fn = "/tmp/.hcsay"+str(TalkID+random.random())
	myfile = open(fn,"w+")	
	myfile.write(user+" has parted from "+msg)
	myfile.close()
	timerThread=threading.Thread(target=TalkTimer, args=(fn,))
	timerThread.start()
	subprocess.Popen(["espeak","-f",fn])
	return hexchat.EAT_NONE
def PMSGTalk(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		# strips the colours and the format
		word[i] = hexchat.strip(word[i], -1, 3)
	# in "word", the first part is the user who issued the message
	user = word[0]
	msg = word[1][0:]
	fn = "/tmp/.hcsay"+str(TalkID+random.random())
	myfile = open(fn,"w+")	
	myfile.write(user+" whispered "+msg)
	myfile.close()
	timerThread=threading.Thread(target=TalkTimer, args=(fn,))
	timerThread.start()
	subprocess.Popen(["espeak","-f",fn])
	return hexchat.EAT_NONE
def QTalk(word, word_eol, userdata):
	# STRIP word
	for i in range(len(word)):
		# strips the colours and the format
		word[i] = hexchat.strip(word[i], -1, 3)
	# in "word", the first part is the user who issued the message
	user = word[0]
	msg = word[1][0:]
	fn = "/tmp/.hcsay"+str(TalkID+random.random())
	myfile = open(fn,"w+")	
	myfile.write(user+" quit chat "+msg)
	myfile.close()
	timerThread=threading.Thread(target=TalkTimer, args=(fn,))
	timerThread.start()
	subprocess.Popen(["espeak","-f",fn])
	return hexchat.EAT_NONE
# Finally, the hook that will link the function above to the action of receiving a channel message
hexchat.hook_print("Channel Message", MSGTalk)
hexchat.hook_print("Private Message to Dialog", PMSGTalk)
hexchat.hook_print("Join", JoinTalk)
hexchat.hook_print("Change Nick", NickTalk)
hexchat.hook_print("Part with Reason", PartTalk)
hexchat.hook_print("Private Action to Dialog", ATalk)
hexchat.hook_print("Channel Action", ATalk)
hexchat.hook_print("Channel Msg Hilight", MSGTalk)
hexchat.hook_print("Quit", QTalk)
# You can find the words "Channel Message" and many other events in HexChat menu "Settings > Text Events..."
