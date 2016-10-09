#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
With this little script we
can send message to telegram
trough a bot we've created with
@BotFather on telegram.
Useful if you are limited

Author: Habb0n
Last modified: October 2016
Github: https://github.com/GooogIe
"""

import urllib2
import os.path
import json
from Tkinter import *
from ttk import Frame,Label,Entry
import tkMessageBox

class gui(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.master = master
		self.initUI()
	
	def initUI(self):
		self.master.title("Telegram UnlimitMe")
		self.master.minsize(width=300,height=130)
		self.pack(fill=BOTH,expand=True)
		
		frame1 = Frame(self)
		frame1.pack(fill=X)

		tknlbl = Label(frame1,text="Token",width=7)
		tknlbl.pack(side=LEFT,padx=5,pady=5)
		
		tkntxt = Entry(frame1)
		tkntxt.pack(fill=X,padx=5,expand = True)
		tkntxt.insert(0,self.loadtoken())
		
		frame2 = Frame(self)
		frame2.pack(fill=X)
		
		cidlbl = Label(frame2,text="Chat ID",width=7)
		cidlbl.pack(side=LEFT,padx=5,pady=5)
		
		cidtxt = Entry(frame2)
		cidtxt.pack(fill=X,padx=5,expand=True)
		cidtxt.insert(0,self.loadcid())
		
		frame3 = Frame(self)
		frame3.pack(fill=X)
		
		msglbl = Label(frame3,text="Message",width=8)
		msglbl.pack(side=LEFT,anchor=N,padx=5,pady=5)
		
		msgtxt = Entry(self,width=30)
		msgtxt.insert(0,"Message to be sent here")
		msgtxt.pack(fill=BOTH,padx=5,pady=2)
		
		frame7 = Frame(self)
		frame7.pack(fill=X)
		
		imglbl = Label(frame7,text="Image Source",width=15)
		imglbl.pack(side=LEFT,anchor=N,padx=5,pady=5)
		
		imgtxt = Entry(self,width=30)
		imgtxt.insert(0,"http://www.photo.it/ok.png")
		imgtxt.pack(fill=BOTH,padx=5,pady=2)
		
		frame4 = Frame(self)
		frame4.pack(fill=X)


		x = StringVar()
		x.set("Chat IDS found: \n"+chatids(tkntxt.get()))
		cidslbl = Label(frame4,textvariable=x,width=35)
		cidslbl.pack(side=LEFT,anchor=N,padx=5,pady=5)
		
		listbox = Listbox(frame4,width= 30)
		listbox.pack(side=RIGHT,padx=5,pady=5)
		
		frame5 = Frame(self)
		frame5.pack(fill=X)
		
		sendbtn = Button(frame5,text="Send",width=12,command=lambda: self.sendMessage(msgtxt.get(),tkntxt.get(),cidtxt.get()) & listbox.insert(END,"You: "+msgtxt.get()))
		sendbtn.pack(side=RIGHT,padx=5,pady=5)
		
		imgbtn = Button(frame5,text="Send a Photo",width=12,command=lambda: self.sendImage(imgtxt.get(),tkntxt.get(),cidtxt.get()))
		imgbtn.pack(side=LEFT,padx=5,pady=5)
		
		savebtn = Button(frame5,text="Save CID & Token",width=12,command=lambda: self.saveall(tkntxt.get(),cidtxt.get()))
		savebtn.pack(side=LEFT,padx=5,pady=5)

		getcidsbtn = Button(frame5,text="Reload Chat IDS",width=12,command=lambda: x.set("Chat IDS found: \n"+chatids(tkntxt.get())))
		getcidsbtn.pack(side=LEFT,padx=5,pady=5)
		
		frame6 = Frame(self)
		frame6.pack(fill=X,expand=True)
		
		abtlbl = Label(frame6,text="Created by Habb0n - (c) 2016 - Using Python & Tkinter",width=50)
		abtlbl.pack(side=BOTTOM,anchor=N,padx=1,pady=1)

	
	def loadtoken(self):
		tokenfile = "token.txt"
		if os.path.exists(tokenfile) != True:
			token = "Paste Bot Token here."
		else:
			stoken = open(tokenfile,'r')
			token = stoken.read()
		return token
		
	def loadcid(self):
		cidfile = "cid.txt"
		if os.path.exists(cidfile) != True:
			cid="Paste Chat ID here."
		else:
			scid = open(cidfile,'r')
			cid = scid.read()
		return cid
	
	def sendMessage(self,message,token,cid):
		chatids(token)
		try:
			url =  "https://api.telegram.org/bot" + token + "/sendMessage?text=" + message + "&chat_id=" + cid+"&parse_mode=Markdown"
			urllib2.urlopen(url).read()
		except:
			tkMessageBox.showinfo('Telegram UlimitMe',"Couldn't send message.\nHave you checked that the token and chat id that you're using are valid?")
		
	def sendImage(self,image,token,cid):
		try:
			url =  "https://api.telegram.org/bot" + token + "/sendPhoto?chat_id=" + cid+"&photo=" +image
			urllib2.urlopen(url).read()
		except:
			tkMessageBox.showinfo('Telegram UlimitMe',"Couldn'tt send image.\nHave you checked that the token and chat id that you're using are valid?\nis the url you provided ending with the image format(.png,.jpg etc...)?")
		
	def saveall(self,token,cid):
		fcid = open('cid.txt','w+')
		fcid.write(cid)
		fcid.close()
		ftoken = open('token.txt','w+')
		ftoken.write(token)
		ftoken.close()

def chatids(token):
	if os.path.exists("token.txt") == True:
		url =  "https://api.telegram.org/bot" + token + "/getUpdates"
		response = urllib2.urlopen(url).read()
		response = json.loads(response)
		cids = []
		i = 0
		while i+2< len(response['result']):
			try:
				id = response['result'][i]['message']['chat']['id']
				name = response['result'][i]['message']['chat']['title']
			except KeyError, e: #Thanks to @Aya - http://stackoverflow.com/questions/16154032/catch-keyerror-in-python
    				pass
			id = str(id)+":"+name.encode('ascii', 'ignore')
			
			if id not in cids:
				cids.append(id)
			else:
				pass	
			i +=1
		i =0
		for ids in cids:
			idcomp = ids.split(':',1)
			idint = int(idcomp[0])
			if idint>0:
				cids.pop(i)
			else:
				pass
			i +=1
		return '\n'.join(cids)
	else:
		return "Please provide a token before."
def main():
	import sys

	req_version = (2,10)
	cur_version = sys.version_info
	print cur_version
	if cur_version < req_version:
		root = Tk()
		try:
			root.iconbitmap('py.ico')
		except:
			pass
		root.resizable(height=False,width=False)
		unlimit = gui(root)
		root.mainloop() 
		root.update_idletasks()
	else:
		print "Your Python interpreter is too new. Please consider downgrading to 2.10 or older."

		

if __name__ == '__main__':
    main()
