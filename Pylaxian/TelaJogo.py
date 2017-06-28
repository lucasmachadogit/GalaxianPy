import pygame
from pygame.locals import *
from Tela import Tela

pygame.init()

class TelaJogo(Tela):
	def __init__(self):
		Tela.__init__(self)

		try:
			self.__texto = pygame.font.Font("PressStart2P.ttf", 12)
			self.__msg = pygame.font.Font("PressStart2P.ttf", 15)
		except IOError:
			print("Não foi possível carregar a fonte do jogo!!")

		self.__cor = (223, 31, 31)
		self.__start = self.__texto.render("Iniciar", True, Tela.getCorObjeto(self))
		self.__voltar = self.__texto.render("Voltar", True, Tela.getCorObjeto(self))
		self.__frase = self.__msg.render("Pronto para missão?", True, self.__cor)

	def escolhaJogo(self, seleciona):
		if seleciona == 0:
			pygame.draw.rect(Tela.getTela(self), Tela.getCorClaro(self), (335,315,105,25))
		else:
			pygame.draw.rect(Tela.getTela(self),Tela.getCorClaro(self), (335,340,105,25))
		
		Tela.getTela(self).blit(self.__frase, (250, 230))	
		Tela.getTela(self).blit(self.__missao, (220, 260))
		Tela.getTela(self).blit(self.__start, (350, 320))
		Tela.getTela(self).blit(self.__voltar, (350, 345))
