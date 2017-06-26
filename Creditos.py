import pygame
from pygame.locals import *
from Tela import Tela
from Textos import Textos

pygame.init()


class Creditos(Tela, Textos):
	def __init__(self):
		Textos.__init__(self)
		Tela.__init__(self)

		try:
			self.__fonte_creditos = pygame.font.Font("PressStart2P.ttf", 15)
		except IOError:
			print("Não foi possível carregar fonte do jogo!!")
			
		self.__volta_menu = self.__fonte_creditos.render("Pressione V para voltar ao menu", True, Tela.getCorObjeto(self))
		self.__text1 = self.__fonte_creditos.render(Textos.getT1(self), True, Tela.getCorCreditos(self))
		self.__text2 = self.__fonte_creditos.render(Textos.getT2(self), True, Tela.getCorCreditos(self))
		self.__text3 = self.__fonte_creditos.render(Textos.getT3(self), True, Tela.getCorCreditos(self))
		self.__text4 = self.__fonte_creditos.render(Textos.getT4(self), True, Tela.getCorCreditos(self))
		self.__text5 = self.__fonte_creditos.render(Textos.getT5(self), True, Tela.getCorCreditos(self))
		self.__text6 = self.__fonte_creditos.render(Textos.getT6(self), True, Tela.getCorCreditos(self))
		self.__text7 = self.__fonte_creditos.render(Textos.getT7(self), True, Tela.getCorCreditos(self))
		self.__text8 = self.__fonte_creditos.render(Textos.getT8(self), True, Tela.getCorCreditos(self))
		self.__text9 = self.__fonte_creditos.render(Textos.getT9(self), True, Tela.getCorCreditos(self))
		
	def Creditos(self):
		Tela.getTela(self).blit(self.__text1, (70, 50))
		Tela.getTela(self).blit(self.__text2, (70, 70))
		Tela.getTela(self).blit(self.__text3, (70, 100))
		Tela.getTela(self).blit(self.__text4, (70, 160))
		Tela.getTela(self).blit(self.__text5, (70, 190))
		Tela.getTela(self).blit(self.__text6, (70, 220))
		Tela.getTela(self).blit(self.__text7, (70, 250))
		Tela.getTela(self).blit(self.__text8, (70, 330))
		Tela.getTela(self).blit(self.__text9, (70, 360))
		Tela.getTela(self).blit(self.__volta_menu, (70, 550))
	
