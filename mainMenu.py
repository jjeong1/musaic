import pygame
from starter import PygameGame
from GameObject import GameObject

class mainMenu(PygameGame):
    def init(self):
        self.background = pygame.image.load("imgs/mainMenuBG.png")
        pygame.mixer.init()
        self.music = pygame.mixer.music.load("music/Whimsical-Popsicle.mp3")
        pygame.mixer.music.play(100,0)
        #dimensions of UI buttons
        self.startDims = (60,145,327,356) #(0:x1, 1:x2, 2:y1, 3:y2)
        self.configDims = (60,284,375,407)
        self.infoDims = (60,130,418,447)
        self.quitDims = (60,136,460,495)
        self.startPressed = False
        self.configPressed = False
        self.infoPressed = False
        self.quitPressed = False

    # Keyboard Functions:
    def keyPressed(self, code, mod): pass

    def keyReleased(self, code, mod): pass

    # Mouse Functions:

    def mousePressed(self, x, y):
    	(thisX,thisY) = pygame.mouse.get_pos()
    	#if user presses "start"
    	if (self.startDims[0]<=thisX <= self.startDims[1] and
    		self.startDims[2] <= thisY <= self.startDims[3]):
    		self.startPressed = True
    		#Start Game Here
    		pass
    	elif (self.configDims[0]<=thisX <= self.configDims[1] and 
    		self.configDims[2] <= thisY <= self.configDims[3]):
    		#Config Screen TBM
    		self.configPressed = True
    		pass
    	elif (self.infoDims[0]<=thisX <= self.infoDims[1] and 
    		self.infoDims[2] <= thisY <= self.infoDims[3]):
    		#Info Screen TBM
    		self.infoPressed = True
    		pass
    	elif (self.quitDims[0]<=thisX <= self.quitDims[1] and 
    		self.quitDims[2] <= thisY <= self.quitDims[3]):
    		self.quitPressed = True
    		pygame.quit()
    	else: pass

    def mouseReleased(self, x, y): pass

    def mouseMotion(self, x, y): pass

    def mouseDrag(self, x, y): pass

    # View:
    def redrawAll(self,screen):
        screen.blit(self.background,(0,0))
        self.background = pygame.transform.scale(self.background, (600,600)).convert_alpha()




mainMenu(600, 600).run()