import pygame
import time
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
		self.__municao = self.__fonte.render("Disparos", True, Tela.getCorCreditos(self))

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

	def temporizador(self, milisegundo, segundo, minuto):
		milisegundo += 1

		if milisegundo >= 60:
			milisegundo = 0
			segundo += 1

		if segundo >= 60:
			segundo = 0
			minuto += 1

		m = self.__fonte_score.render(str(minuto), True, self.__cor_score)
		Tela.getTela(self).blit(m, (35, 30))

		temp = self.__fonte_score.render(":", True, self.__cor_score)
		Tela.getTela(self).blit(temp, (55, 30))

		s = self.__fonte_score.render(str(segundo), True, self.__cor_score)
		Tela.getTela(self).blit(s, (68, 30))

		temp = self.__fonte_score.render(":", True, self.__cor_score)
		Tela.getTela(self).blit(temp, (95, 30))

		mili = self.__fonte_score.render(str(milisegundo), True, self.__cor_score)
		Tela.getTela(self).blit(mili, (110, 30))

		return segundo, minuto, milisegundo

	def statusGameOver(self):
		jogarDeNovo = self.__fonte_score.render("Pressione S para sair/voltar", True, Tela.getCorCreditos(self))
		Tela.getTela(self).blit(jogarDeNovo, (70, 570))
