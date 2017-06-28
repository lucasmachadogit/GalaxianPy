import pygame
from pygame.locals import *
from Tiro import Tiro

pygame.init()

class Nave(object):
	def __init__(self):
		try:
			self.nave = pygame.image.load('nave/nave.png')
		except IOError:
			print("Não foi possível carregar a nave!!")
		
		self.__velocidade = 10
		self.lista_disparo = []
	
	def getNave(self):
		return self.nave
	
	def getVelocidade(self):
		return self.__velocidade

	def disparar(self, x, y):
		tiro = Tiro(x, y)
		self.lista_disparo.append(tiro)
		