import pygame,sys
import pygame.mouse
import button
import math  # for checking for collisions with the mouse and the circle
import random
from pygame.locals import * 
from PIL import Image
pygame.init()


#WIDTH AND HEIGHT OF THE SCREEN
screen_width, screen_height = 1366,768 

#GLOBAL VARIABLE FOR COLOR TO USE
white = (255, 255, 255)

#CLOCK FOR REFRESH RATE OF THE SCREEN
clock = pygame.time.Clock()

#FUNCTION FOR SIMPLIFYING TEXT CREATOR 
def textCreator(textSize,textToDisplay,color,style = None):
	titleTextFont = pygame.font.Font( style, textSize)
	titleText= titleTextFont.render(textToDisplay,True,color)
	return titleText

#FUNCTION FOR THE START OF THE GAME AND MAIN SCREEN
def mainScreen():
	
	#creates a screen by taking the values of width and height according to system compatbility
	screen = pygame.display.set_mode((screen_width,screen_height))
	pygame.display.set_caption('AIMLAB CLONE')

	#IMAGE FOR BACKGROUND AND CONVERTS THE RESOLUTION FOR THE GIVEN SCREEN RATIO
	img = Image.open('mainBackground/mainBackground/titleBackgroundScreen.png')
	img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
	img.save('mainBackground/resized/titleBackgroundScreen.png')
	
	#background of the title screen
	backgroundOfTitleScreen=pygame.image.load('mainBackground/resized/titleBackgroundScreen.png').convert()

	#TITLE ON THE SCREEN(AIMLAB)
	mainTitle = textCreator(60,'A I M L A B',white)
	
	#AIMLAB ICON IN PNG FORMAT
	aimlabIcon=pygame.image.load('mainBackground/gameIcon/aimLabIcon.png').convert_alpha()

	#PLAYBUTTON
	play_Button = button.Button(screen_width/9.8,screen_height/8,textCreator(80,'P L A Y',white))

	#EXIT BUTTON
	quit_Button = button.Button(screen_width/9.8,screen_height/4,textCreator(70,'Q U I T',white)) 

    #Running variable for the program to run continously
	running = True

	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT :
	 			pygame.quit()
	 			sys.exit()
	 			
			if event.type == KEYDOWN :
	 			if event.key == K_ESCAPE:
						running = False
		screen.blit(backgroundOfTitleScreen,(0,0))		
		screen.blit(mainTitle,(screen_width/1.29,screen_height-90))
		screen.blit(aimlabIcon,(screen_width/1.45,screen_height-119))
		
		if play_Button.display(screen):
	 			gameStart()
		if 	quit_Button.display(screen):
				running = False	
		pygame.display.update()

		clock.tick(60)

#FUNCTION WHEN THE GAME STARTS
def gameStart():
	
	display = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('AIMLAB CLONE')
	
	#FUNCTION FOR GENERATING RANDOM BACKGROUND
	def randomBackground():
    	#BACKGROUNDS FOR GAME AND STORING THEM IN LIST FOR RANDOM GENERATION
		background1 = 'blackOsu.png'
		background2 = 'planet.png'
		background3 = 'space1.png'
		background4 = 'space2.png'
		background5 = 'themeBackground.png'
		background6 = 'black.png'
		background7 = 'world.png'
		background8 = 'goldPlanet.png'
		background9 = 'orangeSky.png'
		backgrounds = [background1 , background2 , background3 , background4 , background5 , background6 , background7, background8, background9]
		randomChoosedBackground = random.choice(backgrounds)
		return randomChoosedBackground

	#FUNCTION FOR ATTACHING THE ROOT PATH AND PATH OF THE IMAGES
	def imagePathChange( imagePath, imageLocation):
		path = imagePath+imageLocation
		return path

	#FUNCTION FOR CONVERTING THE IMAGE ACCORDING TO SCREEN WIDTH AND HEIGHT
	def imageConvertorForGameBackground():
		imageLocation = randomBackground()
		originalImagePath = 'gameBackgrounds/gameBackgrounds/'
		resizedImagePath = 'gameBackgrounds/resizedBackgrounds/'
		img = Image.open(imagePathChange(originalImagePath, imageLocation))
		img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
		img.save(imagePathChange(resizedImagePath, imageLocation))
		backgroundOfScreen=pygame.image.load(imagePathChange(resizedImagePath, imageLocation)).convert()
		return backgroundOfScreen

	#BACKGROUND FOR THE GAME
	backgroundDisplay = imageConvertorForGameBackground()
	display.blit(backgroundDisplay,(0,0))

	#FOR GENERATING CIRCLE FOR RANDOM X AND Y AXIS 
	cx = random.randint(100, screen_width - 100)
	cy = random.randint(100, screen_height - 80)
	width_of_circle = 30 
	pygame.draw.circle(display, white, (cx, cy), width_of_circle)

	#SCORE TEXT
	global scoreOfGame
	scoreOfGame = 0
	scoreFontText = textCreator(60, 'SCORE : ' + str(scoreOfGame), white, style = 'font/ChakraPetch-Bold.ttf')
	
	#MISS TEXT
	global missClicks
	missClicks = 5
	missText = textCreator(40,'MISSES LEFT : '+str(missClicks),white,style = 'font/ChakraPetch-Bold.ttf')
	
	#PAUSE BUTTON IN THE GAME SCREEN
	pause_Button = button.Button(screen_width - 220,10,textCreator(60,'PAUSE',white, style = 'font/ChakraPetch-Bold.ttf'))

	gameRunning = True

	# Main loop
	while gameRunning:

		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		click = pygame.mouse.get_pressed()

		sqx = (x - cx)**2
		sqy = (y - cy)**2
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					optionMenu()
					if gameExit == 1:
						gameRunning = False
					if gameExit != 1:
						display.blit(backgroundDisplay,(0,0))
						pygame.draw.circle(display, white, (cx, cy), width_of_circle)
			#THIS IF BLOCK IS USED TO CHECK THE MISSES OF THE PLAYER 			
			if not(math.sqrt(sqx + sqy) < width_of_circle) :	
				if event.type == pygame.MOUSEBUTTONDOWN :
					display.blit(backgroundDisplay,(0,0))
					missClicks = missClicks - 1
					width_of_circle = 30
					missText = textCreator(45,'MISSES LEFT : '+str(missClicks),white,style = 'font/ChakraPetch-Bold.ttf')
					pygame.draw.circle(display, white, (cx, cy), width_of_circle)
					pygame.display.update()

		scoreFontText = textCreator(60, 'SCORE : ' + str(scoreOfGame), white, style = 'font/ChakraPetch-Bold.ttf')
		display.blit(scoreFontText,(10,10))
		missText = textCreator(45,'MISSES LEFT : '+str(missClicks),white,style = 'font/ChakraPetch-Bold.ttf')
		display.blit(missText,(screen_width/2.6,20))
		
		#THIS IF BLOCK IS USED TO CHECK THE CLICKS OF THE CIRCLES
		if math.sqrt(sqx + sqy) < width_of_circle and click[0] == 1:
			display.blit(backgroundDisplay,(0,0))  # Reset the screen
			scoreOfGame = scoreOfGame + 1
			cx = random.randint(100, screen_width - 100)
			cy = random.randint(100, screen_height - 80)
			width_of_circle = 30
			pygame.draw.circle(display, white, (cx, cy), width_of_circle)

		if pause_Button.display(display):
			
			missClicks = missClicks + 1
			optionMenu()
			if gameExit == 1:
				gameRunning = False
			if gameExit != 1:
				display.blit(backgroundDisplay,(0,0))
				pygame.draw.circle(display, white, (cx, cy), width_of_circle)

		if missClicks <= 0:
			scoreScreen(scoreOfGame,missClicks)
			gameRunning = False
		
		pygame.display.update()
		clock.tick(120)

#FUNCTION FOR PAUSE MENU
def optionMenu():

	optionScreen = pygame.display.set_mode((screen_width,screen_height))
	pygame.display.set_caption('AIMLAB CLONE')

	#IMAGE FOR BACKGROUND AND CONVERTS THE RESOLUTION FOR THE GIVEN SCREEN RATIO
	img = Image.open('optionBackground/imageFile/optionBackground.png')
	img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
	img.save('optionBackground/resizedImage/optionBackground.png')
	
	#BACKGROUND OF THE SCREEN
	backgroundOfOptionScreen=pygame.image.load('optionBackground/resizedImage/optionBackground.png').convert()

	#FONT FOR OPTION MENU
	aimlabDisplay = textCreator(80,'A I M L A B',white)

	#BUTTON FOR CONTINUE OPTION
	continue_Button = button.Button(100,200,textCreator(70,'CONTINUE',white))

	#BUTTON FOR EXIT BUTTON
	exit_Button = button.Button(100,280,textCreator(70,'EXIT',white))

	global gameExit
	gameExit = 0

	optionMenuRunning = True

	while optionMenuRunning :
		for event in pygame.event.get():
			if event.type == KEYDOWN :
	 			if event.key == K_ESCAPE:
						optionMenuRunning = False
		optionScreen.blit(backgroundOfOptionScreen,(0,0))
		optionScreen.blit(aimlabDisplay,(100,100))
		if continue_Button.display(optionScreen):
			optionMenuRunning = False
		if exit_Button.display(optionScreen):
			decisionMenu()
			if exit == 1:
				gameExit = 1
				optionMenuRunning = False
		pygame.display.update()
		clock.tick(120)	

#FUNCTION FOR DECISION TO EXIT THE GAME OR NOT		
def decisionMenu():
	scoreDisplay = pygame.display.set_mode((screen_width,screen_height))
	pygame.display.set_caption('AIMLAB CLONE')

	#IMAGE FOR BACKGROUND AND CONVERTS THE RESOLUTION FOR THE GIVEN SCREEN RATIO
	img = Image.open('optionBackground/imageFile/optionBackground.png')
	img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
	img.save('optionBackground/resizedImage/optionBackground.png')

	backgroundOfscoreDisplay=pygame.image.load('optionBackground/resizedImage/optionBackground.png').convert()
	#AIMLAB TEXT FOR OPTION MENU
	aimlabDisplay = textCreator(80,'A I M L A B',white)

	#QUESTION TEXT FOR DECISON STATEMENT
	questionDisplay = textCreator(60,'DO YOU WANT TO EXIT THE GAME ?','#00203FFF')

	#YES BUTTON 
	yesButton = button.Button(screen_width/4,screen_height/2,textCreator(80,'Y E S','#00203FFF'))
	#NO BUTTON
	noButton = button.Button(screen_width/1.6,screen_height/2,textCreator(80,'N O','#00203FFF'))
	
	global exit 
	exit = 0
	
	scoreDisplayRunning = True

	while scoreDisplayRunning:
		for event in pygame.event.get():
			if event.type == KEYDOWN :
	 			if event.key == K_ESCAPE:
						scoreDisplayRunning = False
		scoreDisplay.blit(backgroundOfscoreDisplay,(0,0))				
		scoreDisplay.blit(aimlabDisplay,(100,100))
		scoreDisplay.blit(questionDisplay,(screen_width/4.5,screen_height/2.5))

		if noButton.display(scoreDisplay):
			scoreDisplayRunning = False
		if yesButton.display(scoreDisplay):
			exit = 1
			scoreScreen(scoreOfGame,missClicks)
			scoreDisplayRunning = False
			
		pygame.display.update()
		clock.tick(120)	

#FUNCTION FOR DISPLAYING THE SCORE BOARD		
def scoreScreen(score,miss):

	scoreDisplay = pygame.display.set_mode()
	pygame.display.set_caption('AIMLAB CLONE')
	img = Image.open('scoreBackground/scoreScreenBackground/scoreBackground.png')
	img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
	img.save('scoreBackground/resized/scoreBackground.png')
	
	backgroundOfScoreScreen=pygame.image.load('scoreBackground/resized/scoreBackground.png').convert()

	#PLAY AGAIN BUTTON
	playAgainButton = button.Button(screen_width/20,screen_height/1.19,textCreator(50,'PLAY AGAIN',white))
	#BACK TO MENU BUTTON
	backToMenuButton = button.Button(screen_width/1.45,screen_height/1.19,textCreator(50,'BACK TO MAIN MENU',white))
	
	#AIMLAB DISPLAY
	aimlabDisplay = textCreator(80,'A I M L A B',white)
	#SCORE DISPLAY
	scoreDisplayText = textCreator(70,'SCORE : '+str(score),white)

	scoreScreenRunning = True

	while scoreScreenRunning:
		for event in pygame.event.get():
			if event.type == KEYDOWN :
	 			if event.key == K_ESCAPE:
						scoreScreenRunning = False
		
		scoreDisplay.blit(backgroundOfScoreScreen,(0,0))				
		scoreDisplay.blit(aimlabDisplay,(screen_width/20,screen_height/9))
		scoreDisplay.blit(scoreDisplayText,(screen_width/20,screen_height/4))
		pygame.draw.line(scoreDisplay,white, (screen_width/20,screen_height/1.28), (screen_width/1.04,screen_height/1.28), 5)
		if playAgainButton.display(scoreDisplay):
			gameStart()
			scoreScreenRunning = False
		if backToMenuButton.display(scoreDisplay):
			scoreScreenRunning = False	
		pygame.display.update()
		clock.tick(120)

mainScreen()
pygame.quit()