import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 960
WINDOWHEIGHT = 720
BUTTONHEIGHT = 60
BUTTONWIDTH = 80

TXT1 = 'Welcome to the Virtual Biology Mitosis Lab. During this simulation, we will learn about the stages of Mitosis as well as using the tools accompanying the observation. We will also learn the differences between the animal and the plant cell.'
TXT2 = 'The next page will show you a prepared Onion Root Tip. Your job is to identify the different parts of the onion root tip, mainly the region of cell division, cell elongation and the root cap.'
TXT3 = 'Next, we will learn how to put the Onion Root Tip under the microscope. Your job is to click the right objects in the correct order.'
TXT4 = 'Let\'s take a quick look at Mitosis and its different stages. First, identify the 5 stages of mitosis.'
TXT5 = 'Great! Now that we\'ve zoomed and looked at the cell, it\'s time to finally see the Mitosis in action.'
TXT6 = 'Now that we\'ve prepped the microscope slide, let\'s take a look under the microscope.'

GRAY		= (100, 100, 100)
NAVYBLUE 	= (60, 60, 100)
WHITE		= (255, 255, 255)
RED			= (255, 0, 0)
GREEN		= ( 0, 255, 0)
BLUE 		= (0, 0, 255)
YELLOW		= (255, 255, 0)
ORANGE		= (255, 128, 0)
PURPLE		= (255, 0, 255)
CYAN		= (0, 255, 255)
BLACK		= (0, 0, 0)

BGCOLOR = WHITE
WRONGBGCOLOR = RED
HIGHLIGHTCOLOR = BLUE


# Represents the start page of the simulation. The simulation can be started from here.


def startPage():

	mouseClicked = False	
	
	 
	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Virtual Biology Lab', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.center = (480, 90)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)

	subFontObj = pygame.font.Font('freesansbold.ttf', 48)
	subSurfaceObj = subFontObj.render('Mitosis', True, NAVYBLUE)
	subRectObj = subSurfaceObj.get_rect()
	subRectObj.center = (480, 180)
	DISPLAYSURF.blit(subSurfaceObj, subRectObj)

	startFontObj = pygame.font.Font('freesansbold.ttf', 48)
	startSurfaceObj = startFontObj.render('Start', True, CYAN, BLACK)
	startRectObj = startSurfaceObj.get_rect()
	startRectObj.center = (480, 360)
	DISPLAYSURF.blit(startSurfaceObj, startRectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if startRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (startRectObj.left - 5, startRectObj.top - 5, startRectObj.width + 10, startRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (startRectObj.left - 5, startRectObj.top - 5, startRectObj.width + 10, startRectObj.height + 10), 4)
				
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if startRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT1, nextInstruction, (TXT2, onionRoot1))
	
	
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	
##################################################################
		
# Represents the instruction pages that the student shall read before starting
# the lab simulation. It provides information on what to do and how to do it.

# s must be a string and represents the message that will show up on the
# instruction page. 
# f must be a function and represents the next instruction that the page will be
# brought to.
# args represents the arguments of the next instruction.

def instructionPage(s, f, args = ()):

	mouseClicked = False
	
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Instructions', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)

	textFontObj = pygame.font.Font('freesansbold.ttf', 36)
	textBox = pygame.Rect(90, 90, 870, 585)
	drawText(DISPLAYSURF, s, BLACK, textBox, textFontObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('Next', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
		
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					f(*args)
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)
##############################################################

# Represents the next instruction page to be brought to.

# s must be a string and represents the message that will show up on the
# instruction page. 
# f must be a function and represents the next instruction that the page will be
# brought to.
# args represents the arguments of the next instruction.

def nextInstruction(s, f, args = ()):
	instructionPage(s, f, args)

################################################################


# Represents the first onion root page that deals with the characterizing of
# an onion root. Specifically, it will ask you to determine a specific region.

def interphase():

	mouseClicked = False
	
	
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identify...', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Click the arrow next to the region of cell division:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	rootImg = pygame.image.load('root.png')
	DISPLAYSURF.blit(rootImg, (270, 160))
	
	arrowImg = pygame.image.load('arrow.png')
	DISPLAYSURF.blit(arrowImg, (510, 200))
	DISPLAYSURF.blit(arrowImg, (510, 360))
	DISPLAYSURF.blit(arrowImg, (510, 450))
	
	arrow1rect = pygame.Rect((510, 200), arrowImg.get_size())
	arrow2rect = pygame.Rect((510, 360), arrowImg.get_size())
	arrow3rect = pygame.Rect((510, 450), arrowImg.get_size())
	
	while True:
		
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if arrow1rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow1rect.left - 5, arrow1rect.top - 5, arrow1rect.width + 10, arrow1rect.height + 10), 4)
				elif arrow2rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow2rect.left - 5, arrow2rect.top - 5, arrow2rect.width + 10, arrow2rect.height + 10), 4)
				elif arrow3rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow1rect.left - 5, arrow1rect.top - 5, arrow1rect.width + 10, arrow1rect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow2rect.left - 5, arrow2rect.top - 5, arrow2rect.width + 10, arrow2rect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if arrow2rect.collidepoint(mousex, mousey):
					onionRoot2()
				elif arrow1rect.collidepoint(mousex, mousey) or arrow3rect.collidepoint(mousex, mousey):
					feedback('Oops, looks like you made a mistake, you didn\'t click on the right object. Click Back and try again.', onionRoot1)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	


####################################################################

def onionRoot1():
	mouseClicked = False
	
	
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identify...', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Click the arrow next to the region of cell division:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	rootImg = pygame.image.load('root.png')
	DISPLAYSURF.blit(rootImg, (270, 160))
	
	arrowImg = pygame.image.load('arrow.png')
	DISPLAYSURF.blit(arrowImg, (510, 200))
	DISPLAYSURF.blit(arrowImg, (510, 360))
	DISPLAYSURF.blit(arrowImg, (510, 450))
	
	arrow1rect = pygame.Rect((510, 200), arrowImg.get_size())
	arrow2rect = pygame.Rect((510, 360), arrowImg.get_size())
	arrow3rect = pygame.Rect((510, 450), arrowImg.get_size())
	
	while True:
		
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if arrow1rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow1rect.left - 5, arrow1rect.top - 5, arrow1rect.width + 10, arrow1rect.height + 10), 4)
				elif arrow2rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow2rect.left - 5, arrow2rect.top - 5, arrow2rect.width + 10, arrow2rect.height + 10), 4)
				elif arrow3rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow1rect.left - 5, arrow1rect.top - 5, arrow1rect.width + 10, arrow1rect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow2rect.left - 5, arrow2rect.top - 5, arrow2rect.width + 10, arrow2rect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if arrow2rect.collidepoint(mousex, mousey):
					onionRoot2()
				elif arrow1rect.collidepoint(mousex, mousey) or arrow3rect.collidepoint(mousex, mousey):
					feedback('Oops, looks like you made a mistake, you didn\'t click on the right object. Click Back and try again.', onionRoot1)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
##############################################################

# Represents the second onion root page that deals with the characterizing of
# an onion root. Specifically it will ask you to determine a specific region.
# This function will not be reached unless onionRoot1() successfully
# brings you to this function.

def onionRoot2():
	mouseClicked = False
	
	
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identify...', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Click the arrow next to the region of cell elongation:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	rootImg = pygame.image.load('root.png')
	DISPLAYSURF.blit(rootImg, (270, 160))
	
	arrowImg = pygame.image.load('arrow.png')
	DISPLAYSURF.blit(arrowImg, (510, 200))
	DISPLAYSURF.blit(arrowImg, (510, 360))
	DISPLAYSURF.blit(arrowImg, (510, 450))
	
	arrow1rect = pygame.Rect((510, 200), arrowImg.get_size())
	arrow2rect = pygame.Rect((510, 360), arrowImg.get_size())
	arrow3rect = pygame.Rect((510, 450), arrowImg.get_size())
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Cell Division', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.midleft = (arrow2rect.right + 10, arrow2rect.centery)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	while True:
		
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if arrow1rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow1rect.left - 5, arrow1rect.top - 5, arrow1rect.width + 10, arrow1rect.height + 10), 4)
				elif arrow3rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow1rect.left - 5, arrow1rect.top - 5, arrow1rect.width + 10, arrow1rect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if arrow1rect.collidepoint(mousex, mousey):
					onionRoot3()
				elif arrow3rect.collidepoint(mousex, mousey):
					feedback('Oops, looks like you made a mistake, you didn\'t click on the right object. Click Back and try again.', onionRoot2)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

##############################################################

# Represents the third onion root page that deals with the characterizing of
# an onion root. Specifically it will ask you to determine a specific region.
# This function will not be reached unless onionRoot2() successfully
# brings you to this function.

def onionRoot3():
	mouseClicked = False
	
	
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identify...', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Click the arrow next to the root cap:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	rootImg = pygame.image.load('root.png')
	DISPLAYSURF.blit(rootImg, (270, 160))
	
	arrowImg = pygame.image.load('arrow.png')
	DISPLAYSURF.blit(arrowImg, (510, 200))
	DISPLAYSURF.blit(arrowImg, (510, 360))
	DISPLAYSURF.blit(arrowImg, (510, 450))
	
	arrow1rect = pygame.Rect((510, 200), arrowImg.get_size())
	arrow2rect = pygame.Rect((510, 360), arrowImg.get_size())
	arrow3rect = pygame.Rect((510, 450), arrowImg.get_size())
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Cell Division', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.midleft = (arrow2rect.right + 10, arrow2rect.centery)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Cell Elongation', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.midleft = (arrow1rect.right + 10, arrow1rect.centery)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	while True:
		
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if arrow3rect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow1rect.left - 5, arrow1rect.top - 5, arrow1rect.width + 10, arrow1rect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (arrow3rect.left - 5, arrow3rect.top - 5, arrow3rect.width + 10, arrow3rect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if arrow3rect.collidepoint(mousex, mousey):
					onionRoot4()
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
##############################################################

# Represents the page that tells you if you correctly determined the regions
# of the onion root. This function will not be reached unless onionRoot3()
# successfully brings you to this function. This page will be able to bring
# you to the next set of instructions and next section of the simulation.

def onionRoot4():
	mouseClicked = False
	
	
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Good Job!', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('You correctly identified the Onion Root!', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	rootImg = pygame.image.load('root.png')
	DISPLAYSURF.blit(rootImg, (270, 160))
	
	arrowImg = pygame.image.load('arrow.png')
	DISPLAYSURF.blit(arrowImg, (510, 200))
	DISPLAYSURF.blit(arrowImg, (510, 360))
	DISPLAYSURF.blit(arrowImg, (510, 450))
	
	arrow1rect = pygame.Rect((510, 200), arrowImg.get_size())
	arrow2rect = pygame.Rect((510, 360), arrowImg.get_size())
	arrow3rect = pygame.Rect((510, 450), arrowImg.get_size())
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Cell Division', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.midleft = (arrow2rect.right + 10, arrow2rect.centery)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Cell Elongation', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.midleft = (arrow1rect.right + 10, arrow1rect.centery)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Root Cap', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.midleft = (arrow3rect.right + 10, arrow3rect.centery)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('Next', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
		
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT4, mitosis1)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

		
##############################################################

# Represents the page that tells you to correctly identify objects that are
# needed for the lab.

def prepareMic1():


	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Preparing the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('First, identify the bottom slide', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	slideImg = pygame.image.load('slide.png')
	slideCoverImg = pygame.image.load('slide_cover.png')
	onionRootImg = pygame.image.load('onion_root.png')
	dropperImg = pygame.image.load('blue_dropper.png')
	
	slideRect = pygame.Rect((90, 180), slideImg.get_size()) 
	slideCoverRect = pygame.Rect((90 + 195, 180), slideCoverImg.get_size())
	onionRootRect = pygame.Rect((90 + 390, 180), onionRootImg.get_size())
	dropperRect = pygame.Rect((90 + 585, 180), dropperImg.get_size())
	
	DISPLAYSURF.blit(slideImg, slideRect)
	DISPLAYSURF.blit(slideCoverImg, slideCoverRect)
	DISPLAYSURF.blit(onionRootImg, onionRootRect)
	DISPLAYSURF.blit(dropperImg, dropperRect)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if slideRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (slideRect.left - 5, slideRect.top - 5, slideRect.width + 10, slideRect.height + 10), 4)
				elif slideCoverRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
				elif onionRootRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (onionRootRect.left - 5, onionRootRect.top - 5, onionRootRect.width + 10, onionRootRect.height + 10), 4)
				elif dropperRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (dropperRect.left - 5, dropperRect.top - 5, dropperRect.width + 10, dropperRect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (slideRect.left - 5, slideRect.top - 5, slideRect.width + 10, slideRect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (onionRootRect.left - 5, onionRootRect.top - 5, onionRootRect.width + 10, onionRootRect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (dropperRect.left - 5, dropperRect.top - 5, dropperRect.width + 10, dropperRect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if slideRect.collidepoint(mousex, mousey):
					prepareMic2()
				elif slideCoverRect.collidepoint(mousex, mousey) or dropperRect.collidepoint(mousex, mousey) or onionRootRect.collidepoint(mousex, mousey):
					feedback('Oops, looks like you made a mistake, you didn\'t click on the right object. Click Back and try again.', prepareMic1)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
###############################################################

# Represents the page that tells you to correctly identify objects that are
# needed for the lab. This function will not be reached unless
# prepareMic1() successfully brings you to this function.

def prepareMic2():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Preparing the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Next, click on the root to place on slide.', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	slideImg = pygame.image.load('slide.png')
	slideCoverImg = pygame.image.load('slide_cover.png')
	onionRootImg = pygame.image.load('onion_root.png')
	dropperImg = pygame.image.load('blue_dropper.png')
	
	slideRect = pygame.Rect((480, 540), slideImg.get_size()) 
	slideCoverRect = pygame.Rect((90 + 195, 180), slideCoverImg.get_size())
	onionRootRect = pygame.Rect((90 + 390, 180), onionRootImg.get_size())
	dropperRect = pygame.Rect((90 + 585, 180), dropperImg.get_size())
	
	slideRect.center = (480, 540)
	
	DISPLAYSURF.blit(slideImg, slideRect)
	DISPLAYSURF.blit(slideCoverImg, slideCoverRect)
	DISPLAYSURF.blit(onionRootImg, onionRootRect)
	DISPLAYSURF.blit(dropperImg, dropperRect)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if slideCoverRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
				elif onionRootRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (onionRootRect.left - 5, onionRootRect.top - 5, onionRootRect.width + 10, onionRootRect.height + 10), 4)
				elif dropperRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (dropperRect.left - 5, dropperRect.top - 5, dropperRect.width + 10, dropperRect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (onionRootRect.left - 5, onionRootRect.top - 5, onionRootRect.width + 10, onionRootRect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (dropperRect.left - 5, dropperRect.top - 5, dropperRect.width + 10, dropperRect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if onionRootRect.collidepoint(mousex, mousey):
					prepareMic3()
				elif slideCoverRect.collidepoint(mousex, mousey) or dropperRect.collidepoint(mousex, mousey):
					feedback('Oops, looks like you clicked the wrong object! Click Back to try again.', prepareMic2)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	
###############################################################

# Represents the page that tells you to correctly identify objects that are
# needed for the lab. This function will not be reached unless
# prepareMic2() successfully brings you to this function.
	
def prepareMic3():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Preparing the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Next, click on the dye to drop on the root.', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	slideImg = pygame.image.load('slide.png')
	slideCoverImg = pygame.image.load('slide_cover.png')
	onionRootImg = pygame.image.load('rsz_onion_root.png')
	dropperImg = pygame.image.load('blue_dropper.png')
	
	slideRect = pygame.Rect((480, 540), slideImg.get_size()) 
	slideCoverRect = pygame.Rect((90 + 195, 180), slideCoverImg.get_size())
	onionRootRect = pygame.Rect((90 + 390, 180), onionRootImg.get_size())
	dropperRect = pygame.Rect((90 + 585, 180), dropperImg.get_size())
	
	slideRect.center = (480, 540)
	onionRootRect.center = (480, 540)
	
	DISPLAYSURF.blit(slideImg, slideRect)
	DISPLAYSURF.blit(slideCoverImg, slideCoverRect)
	DISPLAYSURF.blit(onionRootImg, onionRootRect)
	DISPLAYSURF.blit(dropperImg, dropperRect)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if slideCoverRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
				elif dropperRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (dropperRect.left - 5, dropperRect.top - 5, dropperRect.width + 10, dropperRect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (dropperRect.left - 5, dropperRect.top - 5, dropperRect.width + 10, dropperRect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if dropperRect.collidepoint(mousex, mousey):
					prepareMic4()
				elif slideCoverRect.collidepoint(mousex, mousey):
					feedback('Oops, looks like you clicked the wrong object! Click Back to try again.', prepareMic3)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

###############################################################

# Represents the page that tells you to correctly identify objects that are
# needed for the lab. This function will not be reached unless
# prepareMic3() successfully brings you to this function.

def prepareMic4():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Preparing the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Next, cover the slide with the slide cover.', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	slideImg = pygame.image.load('slide.png')
	slideCoverImg = pygame.image.load('slide_cover.png')
	onionRootImg = pygame.image.load('rsz_onion_root.png')
	dyeImg = pygame.image.load('dye.png')
	
	slideRect = pygame.Rect((480, 540), slideImg.get_size()) 
	slideCoverRect = pygame.Rect((90 + 195, 180), slideCoverImg.get_size())
	onionRootRect = pygame.Rect((90 + 390, 180), onionRootImg.get_size())
	dyeRect = pygame.Rect((90 + 585, 180), dyeImg.get_size())
	
	slideRect.center = (480, 540)
	onionRootRect.center = (480, 540)
	dyeRect.center = (480, 540)
	
	DISPLAYSURF.blit(slideImg, slideRect)
	DISPLAYSURF.blit(slideCoverImg, slideCoverRect)
	DISPLAYSURF.blit(onionRootImg, onionRootRect)
	DISPLAYSURF.blit(dyeImg, dyeRect)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if slideCoverRect.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (slideCoverRect.left - 5, slideCoverRect.top - 5, slideCoverRect.width + 10, slideCoverRect.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if slideCoverRect.collidepoint(mousex, mousey):
					prepareMic5()
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
#################################################################

# Represents the page that tells you if you correctly indentified all of the
# objects correctly. This function will not be reached unless
# prepareMic4() successfully brings you to this function. This page will
# be able to bring you to the next set of instructions and next section of the
# simulation.

def prepareMic5():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Good Job!', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('The microscope slide is now ready. Let\'s take a look!', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('Next', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
	
	slideImg = pygame.image.load('slide.png')
	slideCoverImg = pygame.image.load('slide_cover.png')
	onionRootImg = pygame.image.load('rsz_onion_root.png')
	dyeImg = pygame.image.load('dye.png')
	
	slideRect = pygame.Rect((480, 540), slideImg.get_size()) 
	slideCoverRect = pygame.Rect((90 + 195, 180), slideCoverImg.get_size())
	onionRootRect = pygame.Rect((90 + 390, 180), onionRootImg.get_size())
	dyeRect = pygame.Rect((90 + 585, 180), dyeImg.get_size())
	
	slideRect.center = (480, 360)
	onionRootRect.center = (480, 360)
	dyeRect.center = (480, 360)
	slideCoverRect.center = (480, 360)
	
	DISPLAYSURF.blit(slideImg, slideRect)
	DISPLAYSURF.blit(slideCoverImg, slideCoverRect)
	DISPLAYSURF.blit(onionRootImg, onionRootRect)
	DISPLAYSURF.blit(dyeImg, dyeRect)
	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT6, microscope1)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
#################################################################

def microscope1():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Using the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Use the zoom to view the cell', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	z_inFontObj = pygame.font.Font('freesansbold.ttf', 48)
	z_inSurfaceObj = z_inFontObj.render('ZOOM IN', True, CYAN, BLACK)
	z_inRectObj = z_inSurfaceObj.get_rect()
	z_inRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(z_inSurfaceObj, z_inRectObj)
	
	#z_outFontObj = pygame.font.Font('freesansbold.ttf', 48)
	#z_outSurfaceObj = z_outFontObj.render('ZOOM OUT', True, CYAN, BLACK)
	#z_outRectObj = z_outSurfaceObj.get_rect()
	#z_outRectObj.bottomleft = (45, 675)
	#DISPLAYSURF.blit(z_outSurfaceObj, z_outRectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('NEXT', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.midbottom = (480, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
	
	cellImg = pygame.image.load('cell1.jpg')
	
	cellRect = pygame.Rect((480, 540), cellImg.get_size())
	
	cellRect.center = (480, 360)
	
	DISPLAYSURF.blit(cellImg, cellRect)	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				elif z_inRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
				#elif z_outRectObj.collidepoint(mousex, mousey)::
					#pygame.draw.rect(DISPLAYSURF, BLUE, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				#	pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT5, mitosisVideo)
				elif z_inRectObj.collidepoint(mousex, mousey):
					microscope2()
				#elif z_outRectObj.collidepoint(mousex,mousey):
					
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)		
		
#################################################################

def microscope2():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Using the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Use the zoom to view the cell', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	z_inFontObj = pygame.font.Font('freesansbold.ttf', 48)
	z_inSurfaceObj = z_inFontObj.render('ZOOM IN', True, CYAN, BLACK)
	z_inRectObj = z_inSurfaceObj.get_rect()
	z_inRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(z_inSurfaceObj, z_inRectObj)
	
	z_outFontObj = pygame.font.Font('freesansbold.ttf', 48)
	z_outSurfaceObj = z_outFontObj.render('ZOOM OUT', True, CYAN, BLACK)
	z_outRectObj = z_outSurfaceObj.get_rect()
	z_outRectObj.bottomleft = (45, 675)
	DISPLAYSURF.blit(z_outSurfaceObj, z_outRectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('NEXT', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.midbottom = (480, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
	
	cellImg = pygame.image.load('cell2.jpeg')
	
	cellRect = pygame.Rect((480, 540), cellImg.get_size())
	
	cellRect.center = (480, 360)
	
	DISPLAYSURF.blit(cellImg, cellRect)	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				elif z_inRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
				elif z_outRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT5, mitosisVideo)
				elif z_inRectObj.collidepoint(mousex, mousey):
					microscope3()
				elif z_outRectObj.collidepoint(mousex,mousey):
					microscope1()
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)	
		
#################################################################

def microscope3():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Using the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Use the zoom to view the cell', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	z_inFontObj = pygame.font.Font('freesansbold.ttf', 48)
	z_inSurfaceObj = z_inFontObj.render('ZOOM IN', True, CYAN, BLACK)
	z_inRectObj = z_inSurfaceObj.get_rect()
	z_inRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(z_inSurfaceObj, z_inRectObj)
	
	z_outFontObj = pygame.font.Font('freesansbold.ttf', 48)
	z_outSurfaceObj = z_outFontObj.render('ZOOM OUT', True, CYAN, BLACK)
	z_outRectObj = z_outSurfaceObj.get_rect()
	z_outRectObj.bottomleft = (45, 675)
	DISPLAYSURF.blit(z_outSurfaceObj, z_outRectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('NEXT', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.midbottom = (480, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
	
	cellImg = pygame.image.load('cell3.jpeg')
	
	cellRect = pygame.Rect((480, 540), cellImg.get_size())
	
	cellRect.center = (480, 360)
	
	DISPLAYSURF.blit(cellImg, cellRect)	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				elif z_inRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
				elif z_outRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT5, mitosisVideo)
				elif z_inRectObj.collidepoint(mousex, mousey):
					microscope4()
				elif z_outRectObj.collidepoint(mousex,mousey):
					microscope2()
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)	

#################################################################

def microscope4():
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Using the Microscope', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Use the zoom to view the cell', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	#z_inFontObj = pygame.font.Font('freesansbold.ttf', 48)
	#z_inSurfaceObj = z_inFontObj.render('ZOOM IN', True, CYAN, BLACK)
	#z_inRectObj = z_inSurfaceObj.get_rect()
	#z_inRectObj.bottomright = (915, 675)
	#DISPLAYSURF.blit(z_inSurfaceObj, z_inRectObj)
	
	z_outFontObj = pygame.font.Font('freesansbold.ttf', 48)
	z_outSurfaceObj = z_outFontObj.render('ZOOM OUT', True, CYAN, BLACK)
	z_outRectObj = z_outSurfaceObj.get_rect()
	z_outRectObj.bottomleft = (45, 675)
	DISPLAYSURF.blit(z_outSurfaceObj, z_outRectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('NEXT', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.midbottom = (480, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
	
	cellImg = pygame.image.load('cell4.png')
	
	cellRect = pygame.Rect((480, 540), cellImg.get_size())
	
	cellRect.center = (480, 360)
	
	DISPLAYSURF.blit(cellImg, cellRect)	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				#elif z_inRectObj.collidepoint(mousex, mousey):
				#	pygame.draw.rect(DISPLAYSURF, BLUE, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
				elif z_outRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_outRectObj.left - 5, z_outRectObj.top - 5, z_outRectObj.width + 10, z_outRectObj.height + 10), 4)
				#	pygame.draw.rect(DISPLAYSURF, BGCOLOR, (z_inRectObj.left - 5, z_inRectObj.top - 5, z_inRectObj.width + 10, z_inRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT5, mitosisVideo)
				#elif z_inRectObj.collidepoint(mousex, mousey):
				#	microscope4()
				elif z_outRectObj.collidepoint(mousex,mousey):
					microscope3()
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
				
#################################################################

def mitosisVideo():

	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Exploring the Cell', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	movie = pygame.movie.Movie('mitosis.mpg')
	movieRect = pygame.Rect((480,360), (480,360))
	movieRect.center = (480,360)
	movie_screen = pygame.Surface(movie.get_size()).convert()

	movie.set_display(movie_screen, movieRect)
	movie.play()
	
	while True:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        movie.stop()
		        playing = False
		        pygame.quit()
		if not movie.get_busy():
			mitosisRewind()

		DISPLAYSURF.blit(movie_screen, (0,0))
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	
#################################################################
def mitosisRewind():
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Exploring the Cell', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('Would you like to watch again?', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	ReFontObj = pygame.font.Font('freesansbold.ttf', 48)
	ReSurfaceObj = ReFontObj.render('REWIND', True, CYAN, BLACK)
	ReRectObj = ReSurfaceObj.get_rect()
	ReRectObj.bottomleft = (45, 675)
	DISPLAYSURF.blit(ReSurfaceObj, ReRectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('NEXT', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
	
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()	
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
				elif ReRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (ReRectObj.left - 5, ReRectObj.top - 5, ReRectObj.width + 10, ReRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (nextRectObj.left - 5, nextRectObj.top - 5, nextRectObj.width + 10, nextRectObj.height + 10), 4)
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (ReRectObj.left - 5, ReRectObj.top - 5, ReRectObj.width + 10, ReRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					endPage()
				elif ReRectObj.collidepoint(mousex, mousey):
					mitosisVideo()
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)


# Represents the page that tells you to correctly identify the stages of
# mitosis.

def mitosis1():
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identifying the Stages(1)', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('The first drawing(labeled 1) is:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	mitImg = pygame.image.load('mitosis.jpg')
	mitRect = pygame.Rect((480, 360), mitImg.get_size())
	mitRect.midtop = (480, 150)
	DISPLAYSURF.blit(mitImg, mitRect)
	
	text1FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text1SurfaceObj = text1FontObj.render('interphase', True, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.bottomleft = (90, 585)
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
	
	text2FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text2SurfaceObj = text2FontObj.render('prophase', True, BLACK)
	text2RectObj = text2SurfaceObj.get_rect()
	text2RectObj.midbottom = (460, 585)
	DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
	
	text3FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text3SurfaceObj = text3FontObj.render('metaphase', True, BLACK)
	text3RectObj = text3SurfaceObj.get_rect()
	text3RectObj.bottomright = (830, 585)
	DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)
	
	text4FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text4SurfaceObj = text4FontObj.render('anaphase', True, BLACK)
	text4RectObj = text4SurfaceObj.get_rect()
	text4RectObj.midbottom = (275, 630)
	DISPLAYSURF.blit(text4SurfaceObj, text4RectObj)
	
	text5FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text5SurfaceObj = text5FontObj.render('telephase', True, BLACK)
	text5RectObj = text5SurfaceObj.get_rect()
	text5RectObj.midbottom = (645, 630)
	DISPLAYSURF.blit(text5SurfaceObj, text5RectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if text1RectObj.collidepoint(mousex, mousey):
					highlight(text1RectObj)
				elif text2RectObj.collidepoint(mousex, mousey):
					highlight(text2RectObj)
				elif text3RectObj.collidepoint(mousex, mousey):
					highlight(text3RectObj)
				elif text4RectObj.collidepoint(mousex, mousey):
					highlight(text4RectObj)
				elif text5RectObj.collidepoint(mousex, mousey):
					highlight(text5RectObj)
				else:
					unhighlight(text1RectObj)
					unhighlight(text2RectObj)
					unhighlight(text3RectObj)
					unhighlight(text4RectObj)
					unhighlight(text5RectObj)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if text4RectObj.collidepoint(mousex, mousey):
					mitosis2()
				elif text1RectObj.collidepoint(mousex, mousey) or text2RectObj.collidepoint(mousex, mousey) or text3RectObj.collidepoint(mousex, mousey) or text5RectObj.collidepoint(mousex, mousey):
					feedback('That isn\'t correct. Interphase is where the cell prepares itself for the process of cell division. Prophase creates discrete chromosomes. Metaphase pushed the chromosomes toward the middle. Anaphase is when chromosomes are split and the sister chromatids move to opposite poles of the cell. Telephase creates a membrane to separate the cell. Click Back to try again.', mitosis1)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	
##################################################################	

# Represents the page that tells you to correctly identify the stages of
# mitosis. This function will not be reached unless mitosis1()
# successfully brings you to this function.

def mitosis2():
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identifying the Stages(2)', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('The second drawing(labeled 2) is:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	mitImg = pygame.image.load('mitosis.jpg')
	mitRect = pygame.Rect((480, 360), mitImg.get_size())
	mitRect.midtop = (480, 150)
	DISPLAYSURF.blit(mitImg, mitRect)
	
	text1FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text1SurfaceObj = text1FontObj.render('interphase', True, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.bottomleft = (90, 585)
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
	
	text2FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text2SurfaceObj = text2FontObj.render('prophase', True, BLACK)
	text2RectObj = text2SurfaceObj.get_rect()
	text2RectObj.midbottom = (460, 585)
	DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
	
	text3FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text3SurfaceObj = text3FontObj.render('metaphase', True, BLACK)
	text3RectObj = text3SurfaceObj.get_rect()
	text3RectObj.bottomright = (830, 585)
	DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)
	
	text4FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text4SurfaceObj = text4FontObj.render('anaphase', True, BLACK)
	text4RectObj = text4SurfaceObj.get_rect()
	text4RectObj.midbottom = (275, 630)
	DISPLAYSURF.blit(text4SurfaceObj, text4RectObj)
	
	text5FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text5SurfaceObj = text5FontObj.render('telephase', True, BLACK)
	text5RectObj = text5SurfaceObj.get_rect()
	text5RectObj.midbottom = (645, 630)
	DISPLAYSURF.blit(text5SurfaceObj, text5RectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if text1RectObj.collidepoint(mousex, mousey):
					highlight(text1RectObj)
				elif text2RectObj.collidepoint(mousex, mousey):
					highlight(text2RectObj)
				elif text3RectObj.collidepoint(mousex, mousey):
					highlight(text3RectObj)
				elif text4RectObj.collidepoint(mousex, mousey):
					highlight(text4RectObj)
				elif text5RectObj.collidepoint(mousex, mousey):
					highlight(text5RectObj)
				else:
					unhighlight(text1RectObj)
					unhighlight(text2RectObj)
					unhighlight(text3RectObj)
					unhighlight(text4RectObj)
					unhighlight(text5RectObj)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if text2RectObj.collidepoint(mousex, mousey):
					mitosis3()
				elif text1RectObj.collidepoint(mousex, mousey) or text4RectObj.collidepoint(mousex, mousey) or text3RectObj.collidepoint(mousex, mousey) or text5RectObj.collidepoint(mousex, mousey):
					feedback('That isn\'t correct. Interphase is where the cell prepares itself for the process of cell division. Prophase creates discrete chromosomes. Metaphase pushed the chromosomes toward the middle. Anaphase is when chromosomes are split and the sister chromatids move to opposite poles of the cell. Telephase creates a membrane to separate the cell. Click Back to try again.', mitosis2)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
##################################################################	

# Represents the page that tells you to correctly identify the stages of
# mitosis. This function will not be reached unless mitosis2()
# successfully brings you to this function.

def mitosis3():
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identifying the Stages(3)', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('The third drawing(labeled 3) is:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	mitImg = pygame.image.load('mitosis.jpg')
	mitRect = pygame.Rect((480, 360), mitImg.get_size())
	mitRect.midtop = (480, 150)
	DISPLAYSURF.blit(mitImg, mitRect)
	
	text1FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text1SurfaceObj = text1FontObj.render('interphase', True, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.bottomleft = (90, 585)
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
	
	text2FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text2SurfaceObj = text2FontObj.render('prophase', True, BLACK)
	text2RectObj = text2SurfaceObj.get_rect()
	text2RectObj.midbottom = (460, 585)
	DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
	
	text3FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text3SurfaceObj = text3FontObj.render('metaphase', True, BLACK)
	text3RectObj = text3SurfaceObj.get_rect()
	text3RectObj.bottomright = (830, 585)
	DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)
	
	text4FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text4SurfaceObj = text4FontObj.render('anaphase', True, BLACK)
	text4RectObj = text4SurfaceObj.get_rect()
	text4RectObj.midbottom = (275, 630)
	DISPLAYSURF.blit(text4SurfaceObj, text4RectObj)
	
	text5FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text5SurfaceObj = text5FontObj.render('telephase', True, BLACK)
	text5RectObj = text5SurfaceObj.get_rect()
	text5RectObj.midbottom = (645, 630)
	DISPLAYSURF.blit(text5SurfaceObj, text5RectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if text1RectObj.collidepoint(mousex, mousey):
					highlight(text1RectObj)
				elif text2RectObj.collidepoint(mousex, mousey):
					highlight(text2RectObj)
				elif text3RectObj.collidepoint(mousex, mousey):
					highlight(text3RectObj)
				elif text4RectObj.collidepoint(mousex, mousey):
					highlight(text4RectObj)
				elif text5RectObj.collidepoint(mousex, mousey):
					highlight(text5RectObj)
				else:
					unhighlight(text1RectObj)
					unhighlight(text2RectObj)
					unhighlight(text3RectObj)
					unhighlight(text4RectObj)
					unhighlight(text5RectObj)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if text1RectObj.collidepoint(mousex, mousey):
					mitosis4()
				elif text2RectObj.collidepoint(mousex, mousey) or text4RectObj.collidepoint(mousex, mousey) or text3RectObj.collidepoint(mousex, mousey) or text5RectObj.collidepoint(mousex, mousey):
					feedback('That isn\'t correct. Interphase is where the cell prepares itself for the process of cell division. Prophase creates discrete chromosomes. Metaphase pushed the chromosomes toward the middle. Anaphase is when chromosomes are split and the sister chromatids move to opposite poles of the cell. Telephase creates a membrane to separate the cell. Click Back to try again.', mitosis3)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

##################################################################	

# Represents the page that tells you to correctly identify the stages of
# mitosis. This function will not be reached unless mitosis3()
# successfully brings you to this function.

def mitosis4():
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identifying the Stages(4)', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('The fourth drawing(labeled 4) is:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	mitImg = pygame.image.load('mitosis.jpg')
	mitRect = pygame.Rect((480, 360), mitImg.get_size())
	mitRect.midtop = (480, 150)
	DISPLAYSURF.blit(mitImg, mitRect)
	
	text1FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text1SurfaceObj = text1FontObj.render('interphase', True, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.bottomleft = (90, 585)
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
	
	text2FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text2SurfaceObj = text2FontObj.render('prophase', True, BLACK)
	text2RectObj = text2SurfaceObj.get_rect()
	text2RectObj.midbottom = (460, 585)
	DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
	
	text3FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text3SurfaceObj = text3FontObj.render('metaphase', True, BLACK)
	text3RectObj = text3SurfaceObj.get_rect()
	text3RectObj.bottomright = (830, 585)
	DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)
	
	text4FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text4SurfaceObj = text4FontObj.render('anaphase', True, BLACK)
	text4RectObj = text4SurfaceObj.get_rect()
	text4RectObj.midbottom = (275, 630)
	DISPLAYSURF.blit(text4SurfaceObj, text4RectObj)
	
	text5FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text5SurfaceObj = text5FontObj.render('telephase', True, BLACK)
	text5RectObj = text5SurfaceObj.get_rect()
	text5RectObj.midbottom = (645, 630)
	DISPLAYSURF.blit(text5SurfaceObj, text5RectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if text1RectObj.collidepoint(mousex, mousey):
					highlight(text1RectObj)
				elif text2RectObj.collidepoint(mousex, mousey):
					highlight(text2RectObj)
				elif text3RectObj.collidepoint(mousex, mousey):
					highlight(text3RectObj)
				elif text4RectObj.collidepoint(mousex, mousey):
					highlight(text4RectObj)
				elif text5RectObj.collidepoint(mousex, mousey):
					highlight(text5RectObj)
				else:
					unhighlight(text1RectObj)
					unhighlight(text2RectObj)
					unhighlight(text3RectObj)
					unhighlight(text4RectObj)
					unhighlight(text5RectObj)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if text5RectObj.collidepoint(mousex, mousey):
					mitosis5()
				elif text1RectObj.collidepoint(mousex, mousey) or text4RectObj.collidepoint(mousex, mousey) or text3RectObj.collidepoint(mousex, mousey) or text2RectObj.collidepoint(mousex, mousey):
					feedback('That isn\'t correct. Interphase is where the cell prepares itself for the process of cell division. Prophase creates discrete chromosomes. Metaphase pushed the chromosomes toward the middle. Anaphase is when chromosomes are split and the sister chromatids move to opposite poles of the cell. Telephase creates a membrane to separate the cell. Click Back to try again.', mitosis4)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

##################################################################	

# Represents the page that tells you to correctly identify the stages of
# mitosis. This function will not be reached unless mitosis4()
# successfully brings you to this function.

def mitosis5():
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Identifying the Stages(5)', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('The fifth drawing(labeled 5) is:', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	mitImg = pygame.image.load('mitosis.jpg')
	mitRect = pygame.Rect((480, 360), mitImg.get_size())
	mitRect.midtop = (480, 150)
	DISPLAYSURF.blit(mitImg, mitRect)
	
	text1FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text1SurfaceObj = text1FontObj.render('interphase', True, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.bottomleft = (90, 585)
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
	
	text2FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text2SurfaceObj = text2FontObj.render('prophase', True, BLACK)
	text2RectObj = text2SurfaceObj.get_rect()
	text2RectObj.midbottom = (460, 585)
	DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
	
	text3FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text3SurfaceObj = text3FontObj.render('metaphase', True, BLACK)
	text3RectObj = text3SurfaceObj.get_rect()
	text3RectObj.bottomright = (830, 585)
	DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)
	
	text4FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text4SurfaceObj = text4FontObj.render('anaphase', True, BLACK)
	text4RectObj = text4SurfaceObj.get_rect()
	text4RectObj.midbottom = (275, 630)
	DISPLAYSURF.blit(text4SurfaceObj, text4RectObj)
	
	text5FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text5SurfaceObj = text5FontObj.render('telephase', True, BLACK)
	text5RectObj = text5SurfaceObj.get_rect()
	text5RectObj.midbottom = (645, 630)
	DISPLAYSURF.blit(text5SurfaceObj, text5RectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if text1RectObj.collidepoint(mousex, mousey):
					highlight(text1RectObj)
				elif text2RectObj.collidepoint(mousex, mousey):
					highlight(text2RectObj)
				elif text3RectObj.collidepoint(mousex, mousey):
					highlight(text3RectObj)
				elif text4RectObj.collidepoint(mousex, mousey):
					highlight(text4RectObj)
				elif text5RectObj.collidepoint(mousex, mousey):
					highlight(text5RectObj)
				else:
					unhighlight(text1RectObj)
					unhighlight(text2RectObj)
					unhighlight(text3RectObj)
					unhighlight(text4RectObj)
					unhighlight(text5RectObj)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if text3RectObj.collidepoint(mousex, mousey):
					mitosis6()
				elif text1RectObj.collidepoint(mousex, mousey) or text4RectObj.collidepoint(mousex, mousey) or text2RectObj.collidepoint(mousex, mousey) or text5RectObj.collidepoint(mousex, mousey):
					feedback('That isn\'t correct. Interphase is where the cell prepares itself for the process of cell division. Prophase creates discrete chromosomes. Metaphase pushed the chromosomes toward the middle. Anaphase is when chromosomes are split and the sister chromatids move to opposite poles of the cell. Telephase creates a membrane to separate the cell. Click Back to try again.', mitosis5)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

##################################################################	

# Represents the page that tells you if you correctly identified the stages of
# mitosis. This function will not be reached unless **mitosis5()**
# successfully brings you to this function. This page will be able to bring
# you to the end of the simulation.

def mitosis6():
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Great Job!', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)
	
	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('You correctly identified the stages of mitosis!', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	mitImg = pygame.image.load('mitosis.jpg')
	mitRect = pygame.Rect((480, 360), mitImg.get_size())
	mitRect.midtop = (480, 150)
	DISPLAYSURF.blit(mitImg, mitRect)
	
	text1FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text1SurfaceObj = text1FontObj.render('3. interphase', True, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.bottomleft = (90, 585)
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
	
	text2FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text2SurfaceObj = text2FontObj.render('2. prophase', True, BLACK)
	text2RectObj = text2SurfaceObj.get_rect()
	text2RectObj.midbottom = (460, 585)
	DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
	
	text3FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text3SurfaceObj = text3FontObj.render('5. metaphase', True, BLACK)
	text3RectObj = text3SurfaceObj.get_rect()
	text3RectObj.bottomright = (830, 585)
	DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)
	
	text4FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text4SurfaceObj = text4FontObj.render('1. anaphase', True, BLACK)
	text4RectObj = text4SurfaceObj.get_rect()
	text4RectObj.midbottom = (275, 630)
	DISPLAYSURF.blit(text4SurfaceObj, text4RectObj)
	
	text5FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text5SurfaceObj = text5FontObj.render('4. telephase', True, BLACK)
	text5RectObj = text5SurfaceObj.get_rect()
	text5RectObj.midbottom = (645, 630)
	DISPLAYSURF.blit(text5SurfaceObj, text5RectObj)
	
	nextFontObj = pygame.font.Font('freesansbold.ttf', 48)
	nextSurfaceObj = nextFontObj.render('Next', True, CYAN, BLACK)
	nextRectObj = nextSurfaceObj.get_rect()
	nextRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(nextSurfaceObj, nextRectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if nextRectObj.collidepoint(mousex, mousey):
					highlight(nextRectObj)
				else:
					unhighlight(nextRectObj)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if nextRectObj.collidepoint(mousex, mousey):
					instructionPage(TXT3, prepareMic1)
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)
#################################################################

# Represents the end page telling you your grade and how many mistakes were
# made.

def endPage():
	mouseClicked = False
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('The End', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)

	textFontObj = pygame.font.Font('freesansbold.ttf', 30)
	textSurfaceObj = textFontObj.render('You got ' + str(COUNT) + ' incorrect choices.', True, BLACK)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.topleft = (90, 90)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	text1FontObj = pygame.font.Font('freesansbold.ttf', 30)
	text1SurfaceObj = text1FontObj.render('Your final grade is:', True, BLACK)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.topleft = (90, textRectObj.bottom + 10)
	DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
	
	gradeFontObj = pygame.font.Font('freesansbold.ttf', 64)
	gradeSurfaceObj = gradeFontObj.render(getGrade(), True, RED, BLACK)
	gradeRectObj = gradeSurfaceObj.get_rect()
	gradeRectObj.center = (480, 360)
	DISPLAYSURF.blit(gradeSurfaceObj, gradeRectObj)
	
	quitFontObj = pygame.font.Font('freesansbold.ttf', 48)
	quitSurfaceObj = quitFontObj.render('Quit', True, CYAN, BLACK)
	quitRectObj = quitSurfaceObj.get_rect()
	quitRectObj.bottomright = (915, 675)
	DISPLAYSURF.blit(quitSurfaceObj, quitRectObj)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if quitRectObj.collidepoint(mousex, mousey):
					highlight(quitRectObj)
				else:
					unhighlight(quitRectObj)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if quitRectObj.collidepoint(mousex, mousey):
					pygame.quit()
					sys.exit()
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

##################################################################

# Returns the grade of the lab simulation		
def getGrade():
	return str(100 - 5*COUNT)
##################################################################

# Simply puts a highlight of a rectangle over text.
# RectObj represents a rectangle object.
def highlight(RectObj):
	pygame.draw.rect(DISPLAYSURF, BLUE, (RectObj.left - 5, RectObj.top - 5, RectObj.width + 10, RectObj.height + 10), 4)

##################################################################
	
# Simply unhighlights a rectangle over text.
# RectObj represents a rectangle object.
def unhighlight(RectObj):
	pygame.draw.rect(DISPLAYSURF, BGCOLOR, (RectObj.left - 5, RectObj.top - 5, RectObj.width + 10, RectObj.height + 10), 4)

##################################################################

# Represents the page that provides feedback based on the answer chosen.
# s must be a string and represents the feedback message that will be
# shown.
# f must be a function and represents the next page that you will be
# brought to.
# font represents the font of the text on the feedback page.
# args represents the arguments of the next function.

def feedback(s, f, font = 36,  args = ()):
	mouseClicked = False
	global COUNT 
	COUNT += 1
	
	DISPLAYSURF.fill(BGCOLOR)

	titleFontObj = pygame.font.Font('freesansbold.ttf', 64)
	titleSurfaceObj = titleFontObj.render('Feedback', True, PURPLE)
	titleRectObj = titleSurfaceObj.get_rect()
	titleRectObj.topleft = (15, 15)
	DISPLAYSURF.blit(titleSurfaceObj, titleRectObj)

	textFontObj = pygame.font.Font('freesansbold.ttf', font)
	textBox = pygame.Rect(90, 90, 870, 585)
	drawText(DISPLAYSURF, s, BLACK, textBox, textFontObj)
	
	backFontObj = pygame.font.Font('freesansbold.ttf', 48)
	backSurfaceObj = backFontObj.render('Back', True, CYAN, BLACK)
	backRectObj = backSurfaceObj.get_rect()
	backRectObj.bottomleft = (45, 675)
	DISPLAYSURF.blit(backSurfaceObj, backRectObj)
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
				if backRectObj.collidepoint(mousex, mousey):
					pygame.draw.rect(DISPLAYSURF, BLUE, (backRectObj.left - 5, backRectObj.top - 5, backRectObj.width + 10, backRectObj.height + 10), 4)
				else:
					pygame.draw.rect(DISPLAYSURF, BGCOLOR, (backRectObj.left - 5, backRectObj.top - 5, backRectObj.width + 10, backRectObj.height + 10), 4)
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True
				if backRectObj.collidepoint(mousex, mousey):
					f(*args)
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)

##############################################################

# Represents all of the text that is in the simulation.
# surface represents the surface that the text will be on.
# text must be a string and represents the text that will be used.
# color represents the color that the text will be.
# rect represents the rectangle of where the text will go.
# font represents the font of the text.
# aa is always False
# bkg is always None
		
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2
 
    # get the height of the font
    fontHeight = font.size("Tg")[1]
 
    while text:
        i = 1
 
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break
 
        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
 
        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
 
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
 
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
 
        # remove the text we just blitted
        text = text[i:]
 
    return text

##########################################################################

# Represents the main function. All of the previously stated functions will
# only be run by using **main()**. It initializes everything and starts the
# simulation.

def main():
	global FPSCLOCK, DISPLAYSURF, COUNT
	COUNT = 0
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	DISPLAYSURF.fill(BGCOLOR)
	
	
	
	mousex = 0
	mousey = 0
	pygame.display.set_caption('Virtual Biology Lab')
	
	startPage()
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
if __name__ == '__main__':
	main()
