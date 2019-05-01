import pygame
from starter import PygameGame
from GameObject import GameObject

class levelScreen(PygameGame):
	def levelScreen_init(self):
		self.levelScreenCalled = False
		self.background = pygame.image.load("lvlImgs/1.png")
		pygame.mixer.init()
		self.music = pygame.mixer.music.load("music/Whimsical-Popsicle.mp3")
		pygame.mixer.music.play(100,0)
		self.level1Dims = (106,244,185,216) #(0:x1, 1:x2, 2:y1, 3:y2)
		self.level1Pressed = False


	# Keyboard Functions:
	def levelScreen_keyPressed(self, code, mod): pass

	def levelScreen_keyReleased(self, code, mod): pass

	# Mouse Functions:

	def levelScreen_mousePressed(self, x, y):
		(thisX,thisY) = pygame.mouse.get_pos()
		if (self.level1Dims[0]<=thisX <= self.level1Dims[1] and 
			self.level1Dims[2] <= thisY <= self.level1Dims[3]):
			self.level1Pressed = True

	def levelScreen_mouseReleased(self, x, y): pass

	def levelScreen_mouseMotion(self, x, y): pass

	def levelScreen_mouseDrag(self, x, y): pass

	# View:
	def levelScreen_redrawAll(self,screen):
		screen.blit(self.background,(0,0))
		self.background = pygame.transform.scale(self.background, (600,600)).convert_alpha()
