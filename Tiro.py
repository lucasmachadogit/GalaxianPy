import pygame
from pygame.locals import *
from Tela import Tela

pygame.init()

class Tiro(Tela):
	def __init__(self, x, y):
		Tela.__init__(self)

		try:
			self.__tiro = pygame.image.load('nave/tiro.png')
		except IOError:
			print("Não foi possível carregar a imagem do tiro!!")
		
		self.rect = self.__tiro.get_rect()
		self.rect.top = y
		self.rect.left = x
		self.rect.right = x + 5
		self.rect.bottom = y + 5 
		self.velocidadeTiro = 5
	
	def trajetoria(self):
		self.rect.top =	self.rect.top - self.velocidadeTiro

	def desenhaTiro(self):
		Tela.getTela(self).blit(self.__tiro, self.rect)