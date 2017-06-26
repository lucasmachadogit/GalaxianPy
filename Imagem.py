import pygame
import random
from pygame.locals import *

pygame.init()

class Imagem(object):
	def __init__(self):
		try:
			self.__fundo1 = pygame.image.load('images/PlanoFundo1.png').convert()
			self.__fundo2 = pygame.image.load('images/PlanoFundo2.png').convert()
			self.__fundo3 = pygame.image.load('images/PlanoFundo3.png').convert()
			self.__fundo4 = pygame.image.load('images/PlanoFundo4.png').convert()
			self.__fundo5 = pygame.image.load('images/PlanoFundo5.png').convert()
			self.__gameOver = pygame.image.load('images/gameOVer.png').convert()
		except IOError:
			print("Não foi possível carregar imagens do jogo!!")

		self.__vetor_de_imagens = [self.__fundo1, self.__fundo2, self.__fundo3, self.__fundo4, self.__fundo5]

	def getFundoMenu(self):
		return self.__vetor_de_imagens[random.randint(0, 4)]

	def getGameOver(self):
		return self.__gameOver
