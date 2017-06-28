import pygame
from pygame.locals import *

pygame.init()

class Tela(object):
	def __init__(self):
		self.__tela = pygame.display.set_mode((800, 600))
		self.__fundo = (0, 0, 0)
		self.__cor_objeto = (255, 255, 255)
		self.__cor_claro = (20, 0, 50)
		self.__cor_creditos = (255, 255, 255)
	
	def getCorCreditos(self):
		return self.__cor_creditos

	def getCorObjeto(self):
		return self.__cor_objeto

	def getFundo(self):
		return self.__fundo
	
	def getCorClaro(self):
		return self.__cor_claro

	def Fundo(self):
		self.__tela.fill(self.__fundo)

	def getTela(self):
		return self.__tela	
	