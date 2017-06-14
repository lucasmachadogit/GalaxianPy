import pygame
from pygame.locals import *

pygame.init()

class Inimigo(object):
	def __init__(self):

		try:
			self.__imagemInimigo1 = pygame.image.load('inimigo/inimigo1.png')
			self.__imagemInimigo2 = pygame.image.load('inimigo/inimigo2.png')
			self.__imagemInimigo3 = pygame.image.load('inimigo/inimigo3.png')
		except IOError:
			print("Não foi possível carregar imagens dos inimigos!!")

		self.__vetor = [[self.__imagemInimigo1, self.__imagemInimigo2, self.__imagemInimigo3, self.__imagemInimigo3, self.__imagemInimigo1, self.__imagemInimigo2], 
						[self.__imagemInimigo3, self.__imagemInimigo1, self.__imagemInimigo2, self.__imagemInimigo1, self.__imagemInimigo3, self.__imagemInimigo1],
						[self.__imagemInimigo1, self.__imagemInimigo3, self.__imagemInimigo2, self.__imagemInimigo3, self.__imagemInimigo2, self.__imagemInimigo1]]

	def Inimigo(self):
		return self.__vetor	