import pygame
import random
from pygame.locals import *
from Tela import Tela

pygame.init()

class Inimigo(object):
	def __init__(self,x,y):
		Tela.__init__(self)
		
		try:
			self.__imagemInimigo1 = pygame.image.load('inimigo/inimigo1.png')
			self.__imagemInimigo2 = pygame.image.load('inimigo/inimigo2.png')
			self.__imagemInimigo3 = pygame.image.load('inimigo/inimigo3.png')
		except IOError:
			print("Não foi possível carregar imagens dos inimigos!!")

		self.vetor = [self.__imagemInimigo1, self.__imagemInimigo2, self.__imagemInimigo3]
		self.__imagem = self.vetor[random.randint(0,2)]

		self.rect = self.__imagem.get_rect()
		self.rect.top = y
		self.rect.left = x
		self.velocidadeInimigo = 2
		self.rect.right = x + 32
		self.rect.bottom = y + 32  

	def desenha(self):
		Tela.getTela(self).blit(self.__imagem, self.rect)
	
	def trajetoriaInimigo(self):
		self.rect.top = self.rect.top + self.velocidadeInimigo
	
	def ladoEsquerdo(self):
		self.rect.left = self.rect.left - self.velocidadeInimigo	
	
	def ladoDireito(self):
		self.rect.left = self.rect.left + self.velocidadeInimigo	