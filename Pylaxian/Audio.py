import pygame
from pygame.locals import *

pygame.init()

class Audio(object):
	def __init__(self):
		try:
			self.__effect = pygame.mixer.Sound('sounds/efeito.ogg') #carrega o efeito 
			self.__musicaMenu = pygame.mixer.Sound("sounds/musicaJogando.ogg")
			self.__tiroNave = pygame.mixer.Sound("sounds/tiroNave.ogg")
			self.__explosao = pygame.mixer.Sound("sounds/explosao.ogg")
		except IOError:
			print("Não foi possível carregar os áudios!!")

	def tocaEfeito(self):
		return self.__effect.play() #toca efeito

	def tocaMusicaFundo(self):
		return self.__musicaMenu.play(-1) #toca a música de fundo infinitamente

	def paraMusicaFundo(self):
		return self.__musicaMenu.stop() #para a música de fundo
	
	def explosao(self):
		return self.__explosao.play()		 

	def getTiroNave(self):
		return self.__tiroNave.play()