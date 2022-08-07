import pygame

pygame.init()

class Button():
	def __init__(self, x,y,text):
		self.text = text
		self.rect = self.text.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
	def display(self, surface):
		action =False
		#Get the mouse position
		pos = pygame.mouse.get_pos()
		
		#Check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False		

		#Draw the button on the screen
		surface.blit(self.text,(self.rect.x,self.rect.y))

		return action
