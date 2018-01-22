import time as t
from pygame import *
import numpy as np
from random import *
from textbox import TextBox
import webbrowser

green=(0,255,0)
greengrass=(1,166,17)
black=(0,0,0)
white=(255,255,255)
bluesky=(135,206,235)
red=(255,5,5)
bloodred=(138,7,7)
blue=(0,0,255)
darkblue=(0,0,139)

res=[550,250]

init()
window=display.set_mode(res)
clock = time.Clock()

stoper = 0.0

def isdigit(a):
	if a=='0' or a=='1' or a=='2' or a=='3' or a=='4' or a=='5' or a=='6' or a=='7' or a=='8' or a=='9': 
		return True
	else:
		return False


class Button(object):
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",36)
		self.act=False
		
	def event(self):
		pass
		
	def click(self):
		if mouse.get_pressed()[0]:
			if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
				return True

	def draw(self):

		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
			draw.rect(window,green,Rect(self.x,self.y,self.w,self.h),1)
		else:
			draw.rect(window,white,Rect(self.x,self.y,self.w,self.h),1)
		text = self.Font.render(self.text,True,white)
		window.blit(text,(self.x+5,self.y+5))

		
class StoperButton(Button):
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",36)
		self.act=False
		self.stoper=0.0
		self.mem=0.0
	def event(self):
		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
			if not self.act:
				self.stoper=t.time()
				self.act=True
			else:
				self.act=False
				self.mem=float(t.time())-self.stoper
				self.stoper=0.0	

	def print_text(self):
		if self.act:
			res = float(t.time())-self.stoper
			text = self.Font.render(str(np.round(res,3)),True,white)
			window.blit(text,(self.x+5+self.w,self.y+5))
		else:
			text = self.Font.render(str(np.round(self.mem,3)),True,white)
			window.blit(text,(self.x+5+self.w,self.y+5))

def nic (a, b):
	pass
			
class TimerButton(Button):
	def __init__(self,x,y,w,h,text=""):
		self.x=x
		self.y=y
		self.w=w
		self.h=h
		self.text=text
		self.Font=font.SysFont("arial",36)
		self.act=False
		self.time=0.0
		self.start=0.0
		self.counter=0.0
		
	def event(self,text):
		if str(text)!="" and text !=None:
			work = True
			for a in str(text):
				if not isdigit(a):
					work=False
			if work:
				self.time=float(text)
				self.start=t.time()
				self.counter=self.time
				self.act=True
		

	def draw(self):

		if mouse.get_pos()[0]>self.x and mouse.get_pos()[0]<self.x+self.w and mouse.get_pos()[1]>self.y and mouse.get_pos()[1]<self.y+self.h:
			draw.rect(window,green,Rect(self.x,self.y,self.w,self.h),1)
		else:
			draw.rect(window,white,Rect(self.x,self.y,self.w,self.h),1)
		text = self.Font.render(self.text,True,white)
		window.blit(text,(self.x+5,self.y+5))
		
		if self.act:
			
			text = self.Font.render(str(np.round(self.time-(t.time()-self.start),3)),True,white)
			window.blit(text,(self.x+5+self.w,self.y+5))
			if np.round(self.time-(t.time()-self.start),3)<=0:
				self.act=False
				webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

		#self.time = self.time - 1
	
	
s=StoperButton(50,50,150,50,"stoper")	
timer=TimerButton(250,150,150,50,"timer")	

timerbox=TextBox((50,160,150,30),command=nic,clear_on_enter=True,inactive_on_enter=False)



end=False


while not end:
	for zet in event.get():
		if zet.type ==QUIT:
			end=True
		if zet.type==MOUSEBUTTONUP:
			s.event()
			timer.event(timerbox.final)
		timerbox.get_event(zet)

		
	window.fill(black)
	
	timerbox.update()
	timerbox.draw(window)
	
	#if :
	#timer.event(0,timerbox)
	'''for button in buttons:
		button.draw()
	'''
	timer.draw()
	s.draw()
	s.print_text()
	clock.tick(20)
	display.flip()