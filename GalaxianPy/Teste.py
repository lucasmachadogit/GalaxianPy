import pygame
from pygame.locals import *
from Inimigo import Inimigo

pygame.init()

class Teste(object):
	def __init__(self):
		self.lista_inimigo = []
		
	def gerarInimigo(self, x, y):
		inimigo = Inimigo(x, y)
		self.lista_inimigo.append(inimigo)
		