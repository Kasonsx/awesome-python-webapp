# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
import random
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.introduce = Label(self, text='create a random number in range(1~n)')
		self.introduce.pack()
		self.numlb = Label(self, text='Please input a range number:')
		self.numlb.pack()
		self.numInput = Entry(self)
		self.numInput.pack()
		self.alertButton = Button(self, text='Create',command=self.randomNum)
		self.alertButton.pack()

	def randomNum(self):
		num = self.numInput.get()
		if num == None:
			messagebox.showinfo('Message','Please input content!')
		else:
			randNum = random.randint(1,int(num))
			messagebox.showinfo('Message','The random number: %s' %randNum)

app = Application()
app.master.title('Random Number')
app.mainloop()