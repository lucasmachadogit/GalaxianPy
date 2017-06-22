import pygame
from pygame.locals import *
from Tela import Tela

pygame.init()

class Status(Tela):
	def __init__(self):
		Tela.__init__(self)

		try:
			self.__fonte = pygame.font.Font("PressStart2P.ttf", 18)
			self.__fonte_score = pygame.font.Font("PressStart2P.ttf", 13)
		except IOError:
			print("Não foi possível carregar fonte do jogo!!")

		self.__pontos = self.__fonte.render("Pontos", True, Tela.getCorCreditos(self))
		self.__tempo = self.__fonte.render("Tempo", True, Tela.getCorCreditos(self))
		self.__municao = self.__fonte.render("Munição", True, Tela.getCorCreditos(self))

		self.__cor_score = (255, 0, 0)

	def getPontos(self):
		Tela.getTela(self).blit(self.__pontos, (350, 10))

	def getTempo(self):
		Tela.getTela(self).blit(self.__tempo, (30, 10))

	def getMunicao(self):
		Tela.getTela(self).blit(self.__municao, (640, 10))

	def getPontua(self, pontos):
		score = self.__fonte_score.render(str(pontos), True, self.__cor_score)
		Tela.getTela(self).blit(score, (385, 30))

	def getContaMunicao(self, quantMuni):
		muni = self.__fonte_score.render(str(quantMuni), True, self.__cor_score)
		Tela.getTela(self).blit(muni, (700, 30))