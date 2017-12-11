import pygame
import sys
import threading
import random

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800,600))
		pygame.display.set_caption('Python Game')
		self.image=[]
		self.imagerect=[]
		self.vs=pygame.image.load('vs.jpg')         #vs图片加载
		self.j =pygame.image.load('0.jpg')			#剪刀`
		self.s = pygame.image.load('1.jpg')			#石头`
		self.b = pygame.image.load('2.jpg')			#布`
		self.title = pygame.image.load('title.jpg') #题目`
		self.start = pygame.image.load('start.jpg') #开始按钮
		self.exit = pygame.image.load('exit.jpg')	#退出按钮
		for i in range(3):
			jpg = pygame.image.load(str(i)+'.jpg')
			self.image.append(jpg)
		for i in range(3):
			image=self.image[i]
			rect = image.get_rect()
			rect.left = 200*(i+1) +rect.left
			rect.top =400
			self.imagerect.append(rect)
	def Start(self):
		self.screen.blit(self.title,(200,100,400,140))
		self.screen.blit(self.start, (350, 300, 100, 50))
		self.screen.blit(self.exit, (350, 400, 100, 50))
		pygame.display.flip()
		start =1
		while start:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type==pygame.MOUSEBUTTONDOWN:
					if self.isStart()==0:
						start =0
					elif self.isStart()==1:
						sys.exit()
					else:
						pass
				else:
					pass
		self.run()
	def run(self):
		self.screen.fill((0,0,0))
		for i in range(3):
			self.screen.blit(self.image[i],self.imagerect[i])
		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type ==pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.ONMOUSEBUTDOWN()
				else:
					pass
	def isStart(self):
		pos =pygame.mouse.get_pos()
		if pos[0]>350 and pos[0]<450:
			if pos[1]>300 and pos[1]<350:
				return 0
			elif pos[1] >400 and pos[1]<450:
				return 1
			else:
				return 2
		else:
			return 2
	def ONMOUSEBUTDOWN(self):
		self.screen.blit(self.vs,(300,150,140,140))
		pos = pygame.mouse.get_pos()
		if pos[1] > 400 and pos[1]<540:
			if pos[0]>200 and pos[0]<340:
				self.screen.blit(self.image[0],(150,150,140,140))    #剪刀
				self.iswin(0)
			elif pos[0]>400 and pos[0]<540:
				self.screen.blit(self.image[1], (150, 150, 140, 140))#石头
				self.iswin(1)
			elif pos[0]>600 and pos[0]<740:
				self.screen.blit(self.image[2],(150,150,140,140))    #布
				self.iswin(2)
		else:
			pass
	def iswin(self,value):
		num =random.randint(0,2)
		self.screen.blit(self.image[num],(450,150,590,240))
		pygame.display.flip()
		if num==value:	
			self.screen.blit(self.image[num], (300,10,140,70))
		elif num<value:
			if num==0:			#剪刀
				if value ==2:	#布
					self.screen.blit(self.j,  (300,10,140,70))
				else:			#石头
					self.screen.blit(self.s,  (300,10,140,70))
			else: 				#石头vs布
				self.screen.blit(self.b,  (300,10,140,70))
		else:					#num>value
			if num==2:  		#布
				if value ==1:	#石头
					self.screen.blit(self.b, (300,10,140,70))
				else:			#剪刀
					self.screen.blit(self.j,  (300,10,140,70))
			else:				#石头vs布
				self.screen.blit(self.b,  (300,10,140,70))
		pygame.display.flip()
game =Game()
game.Start()
