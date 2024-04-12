import pygame
import time

from pygame.locals import*
from time import sleep

class Sprite():
	def __init__(self, x, y, w, h, images):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.image = pygame.image.load(images)
  
	def update(self):
		return True

	def isLink():
		return False

	def isBrick():
		return False

	def isPot():
		return False

	# def isBoomerang(self):
	# 	return False

	def collision(self, a, b):
		self.a = a;
		self.b = b;
		if self.a.x + self.a.w <= self.b.x:#right of link
			return False
		if self.a.x >= self.b.x + self.b.w:#left of link
			return False
		if self.a.y + self.a.h <= self.b.y:#bottom of link
			return False
		if self.a.y >= self.b.y + self.b.h:#top of link
			return False
		else:
			print('collsion')
			return True
		

class Link(Sprite):
	def __init__(self, x, y, w, h, images):
		super(Link, self).__init__(x, y, w, h, images)
		self.preX = x
		self.preY = y
		self.x = 200
		self.y = 200
		self.w = w
		self.h = h
		self.imageNum = 0

		self.link_images = []
		self.link_images.append(pygame.image.load("link01.png"))
		self.link_images.append(pygame.image.load("link02.png"))
		self.link_images.append(pygame.image.load("link03.png"))
		self.link_images.append(pygame.image.load("link04.png"))
		self.link_images.append(pygame.image.load("link05.png"))
		self.link_images.append(pygame.image.load("link06.png"))
		self.link_images.append(pygame.image.load("link07.png"))
		self.link_images.append(pygame.image.load("link08.png"))
		self.link_images.append(pygame.image.load("link09.png"))
		self.link_images.append(pygame.image.load("link10.png"))
		self.link_images.append(pygame.image.load("link11.png"))
		self.link_images.append(pygame.image.load("link12.png"))
		self.link_images.append(pygame.image.load("link13.png"))
		self.link_images.append(pygame.image.load("link14.png"))
		self.link_images.append(pygame.image.load("link15.png"))
		self.link_images.append(pygame.image.load("link16.png"))
		self.link_images.append(pygame.image.load("link17.png"))
		self.link_images.append(pygame.image.load("link18.png"))
		self.link_images.append(pygame.image.load("link19.png"))
		self.link_images.append(pygame.image.load("link20.png"))
		self.link_images.append(pygame.image.load("link21.png"))
		self.link_images.append(pygame.image.load("link22.png"))
		self.link_images.append(pygame.image.load("link23.png"))
		self.link_images.append(pygame.image.load("link24.png"))
		self.link_images.append(pygame.image.load("link25.png"))
		self.link_images.append(pygame.image.load("link26.png"))
		self.link_images.append(pygame.image.load("link27.png"))
		self.link_images.append(pygame.image.load("link28.png"))
		self.link_images.append(pygame.image.load("link29.png"))
		self.link_images.append(pygame.image.load("link30.png"))
		self.link_images.append(pygame.image.load("link31.png"))
		self.link_images.append(pygame.image.load("link32.png"))
		self.link_images.append(pygame.image.load("link33.png"))
		self.link_images.append(pygame.image.load("link34.png"))
		self.link_images.append(pygame.image.load("link35.png"))
		self.link_images.append(pygame.image.load("link36.png"))
		self.link_images.append(pygame.image.load("link37.png"))
		self.link_images.append(pygame.image.load("link38.png"))
		self.link_images.append(pygame.image.load("link39.png"))
		self.link_images.append(pygame.image.load("link40.png"))
	
	# def draw(self):
	# 	# screen.blit(self.link_images[self.imageNum], (self.link.x, self.link.y))
	# 	self.image = self.link_images[self.imageNum]

	def updateImageNumDown(self):
		if self.imageNum >= 9:
			self.imageNum = 0
		else:
			self.imageNum += 1
		self.image = self.link_images[self.imageNum]
   
	def updateImageNumLeft(self):
		if self.imageNum >= 19 or self.imageNum < 10:
			self.imageNum = 10
		else:
			self.imageNum += 1
		self.image = self.link_images[self.imageNum]
   
	def updateImageNumUp(self):
		if self.imageNum >= 29 or self.imageNum < 20:
			self.imageNum = 20
		else:
			self.imageNum += 1
		self.image = self.link_images[self.imageNum]
   
	def updateImageNumRight(self):
		if self.imageNum >= 39 or self.imageNum < 30:
			self.imageNum = 30
		else:
			self.imageNum += 1
		self.image = self.link_images[self.imageNum]

	def isLink():
		return True

	def preLocation(self):
		self.preX = self.x
		self.preY = self.y

	def pullOut(self, brick):
		#right of link
		if self.x + self.w >= brick.x and self.preX + self.w <= brick.x:
			self.x = brick.x - self.w 
		
		#left of link
		if self.x <= brick.x + brick.y and self.preX >= brick.x + brick.w:
			self.x = brick.x + brick.w
		
		#top of link
		if self.y <= brick.y + brick.h and self.preY >= brick.y + brick.h:
			self.y = brick.y + brick.h
			
		#bottom of link
		if self.y + self.h >= brick.y and self.preY + self.h <= brick.y:
			self.y = brick.y - self.h 
	
	def update(self):
		return True

class Brick(Sprite):
	def __init__(self, x, y, w, h, images):
		super(Brick, self).__init__(x, y, w, h, images)
		self.x = x
		self.y = y
		self.w = w
		self.h = h
  
	def isBrick(self):
		return True

class Pot(Sprite):
	def __init__(self, x, y, w, h, images):
		super(Pot, self).__init__(x, y, w, h, images)
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def isPot(self):
		return True

class Boomerang(Sprite):
	def __init__(self, x, y, w, h, images):
		super(Boomerang, self).__init__(x, y, w, h, images)
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def isBoomerang(self):
		return True


class Model():
	def __init__(self):
		self.link = Link(200,200, 74, 80, "link01.png")
		self.sprites = []
		# self.link = Link(200,200,"link01.png")
		self.sprites.append(self.link)

		#top row of bricks
		self.sprites.append(Brick(0, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(50, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(100, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(150, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(200, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(250, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(300, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(350, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(400, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(450, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(500, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(550, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(600, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(650, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(700, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(750, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(800, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(850, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(900, 0, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 0, 50, 50, "brick.jpg"))
  
		#left border of bricks
		self.sprites.append(Brick(0, 50, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 100, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 150, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 200, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 250, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 300, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 350, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 400, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 450, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 500, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 550, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 600, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 650, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 700, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 750, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 800, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 850, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 900, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(0, 950, 50, 50, "brick.jpg"))
  
		#right border of bricks
		self.sprites.append(Brick(950, 50, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 100, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 150, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 200, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 250, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 300, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 350, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 400, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 450, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 500, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 550, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 600, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 650, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 700, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 750, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 800, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 850, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 900, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(950, 950, 50, 50, "brick.jpg"))
  
		#bottom row of bricks
		self.sprites.append(Brick(50, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(100, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(150, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(200, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(250, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(300, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(350, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(400, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(450, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(500, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(550, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(600, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(650, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(700, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(750, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(800, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(850, 950, 50, 50, "brick.jpg"))
		self.sprites.append(Brick(900, 950, 50, 50, "brick.jpg"))
  
		self.sprites.append(Pot(300, 300, 25, 25, "pot.png"))
  
	
	def update(self):
		for i in self.sprites:
			i.update()
			if isinstance(i, Brick):
				if i.collision(self.link, i):
					self.link.pullOut(i)
			if isinstance(i, Pot):
				if i.collision(self.link, i):
					self.link.pullOut(i)

	

class View():
	def __init__(self, model):
		self.scrollPosX = 0
		self.scrollPosY = 0
		self.scrollPosW = 500
		self.scrollPosH = 500
		screen_size = (500,500)
		self.screen = pygame.display.set_mode(screen_size, 32)
		# self.link_image = pygame.image.load("Link01.png")
		self.model = model

	def update(self):
		self.screen.fill([0,200,100])
		for j in self.model.sprites:
			self.spriteImage = pygame.transform.scale(j.image, (j.w, j.h))
			self.screen.blit(self.spriteImage, (j.x - self.scrollPosX, j.y - self.scrollPosY))
		# self.screen.blit(self.sprites, self.model.rect)
		pygame.display.flip()

class Controller():
	def __init__(self, model, view):
		self.model = model
		self.view = view
		self.keep_going = True

	def update(self):
		self.model.link.preLocation()
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
			elif event.type == KEYUP:
				if event.key == K_LCTRL:
					self.model.sprites.append(Boomerang(self.model.link.x, self.model.link.y, 8, 12, "boomerang1.png"))
				
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.model.link.x -= 5
			self.model.link.updateImageNumLeft()
			if(self.model.link.x < self.view.scrollPosW and self.view.scrollPosX == self.view.scrollPosW):
				self.view.scrollPosX -= self.view.scrollPosW
			
		if keys[K_RIGHT]:
			self.model.link.x += 5
			self.model.link.updateImageNumRight()
			if(self.model.link.x + self.model.link.w > self.view.scrollPosW and self.view.scrollPosX == 0):
				self.view.scrollPosX += self.view.scrollPosW
    
		if keys[K_UP]:
			self.model.link.y -= 5
			self.model.link.updateImageNumUp()
			if(self.model.link.y < self.view.scrollPosH and self.view.scrollPosY == self.view.scrollPosH):
				self.view.scrollPosY -= self.view.scrollPosH
   
		if keys[K_DOWN]:
			self.model.link.y += 5
			self.model.link.updateImageNumDown()
			if(self.model.link.y + self.model.link.h > self.view.scrollPosH and self.view.scrollPosY == 0):
				self.view.scrollPosY += self.view.scrollPosH


print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m, v)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")