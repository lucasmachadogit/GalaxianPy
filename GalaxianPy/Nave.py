import pygame
from pygame.locals import *

pygame.init()

class Nave(object):
	def __init__(self):
		try:
			self.__nave = pygame.image.load('nave/nave.png')
			self.tiro = pygame.image.load('nave/tiro.png')
		except IOError:
			print("Não foi possível carregar a nave!!")
		
		self.rect = self.tiro.get_rect()
		self.rect.top = 0
		self.rect.left = 0
		self.__velocidade = 5
	
	def getNave(self):
		return self.__nave
	
	def getVelocidade(self):
		return self.__velocidade		
	
		