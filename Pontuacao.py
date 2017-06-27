import pygame
import sqlite3
from pygame.locals import *
from BancoDeDados import BancoDeDados
from Tela import Tela

pygame.init()

class Pontuacao(Tela):
	def __init__(self):
		Tela.__init__(self)
		
		try:
			self.__fonte = pygame.font.Font("PressStart2P.ttf", 15)
			self.__titulo = pygame.font.Font("PressStart2P.ttf", 40)
			self.__score = pygame.font.Font("PressStart2P.ttf", 20)
		except IOError:
			print("Não foi possível carregar fonte do jogo!!")

		self.__cor = (255, 63, 63)

		self.__ranking = self.__titulo.render("Ranking", True, Tela.getCorCreditos(self))
		self.__voltar = self.__fonte.render("Pressione V para voltar ao menu", True, Tela.getCorCreditos(self))

	def blitaRanking(self):
		Tela.getTela(self).blit(self.__ranking, (280, 50))
		Tela.getTela(self).blit(self.__voltar, (70, 570))
	
	def ranking(self):
		bd = BancoDeDados()
		bd.buscaNoBanco()
		placar = bd.getPlacar()

		y = 200
		x = 150

		if len(placar) == 0:
			mensagem = self.__score.render("BANCO DE DADOS VAZIO!!", True, self.__cor)
			Tela.getTela(self).blit(mensagem, (200, 300))
		else:
			if len(placar) > 5:
				tamanho = 5
			else:
				tamanho = len(placar)

			for i in range(tamanho):
				aux = placar[i]
				data, tempo, pontos = aux[1], aux[2], aux[3]
				
				temp = self.__score.render(str(data), True, self.__cor)
				Tela.getTela(self).blit(temp, (x, y))

				temp2 = self.__score.render(str(tempo), True, self.__cor)
				Tela.getTela(self).blit(temp2, (x+200, y))

				temp3 = self.__score.render(str(pontos), True, self.__cor)
				Tela.getTela(self).blit(temp3, (x+400, y))

				y += 50