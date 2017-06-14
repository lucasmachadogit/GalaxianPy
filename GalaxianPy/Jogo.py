import pygame
from pygame.locals import *
from Nave import Nave
from Tela import Tela
from Imagem import Imagem
from Inimigo import Inimigo

pygame.init()

class Jogo(Nave, Tela, Imagem, Inimigo):
	def __init__(self):
		Nave.__init__(self)
		Tela.__init__(self)
		Imagem.__init__(self)
		Inimigo.__init__(self)

	def movimentaNave(self,x,y):
		Tela.getTela(self).blit(Nave.getNave(self), (x,y))
	
	def fundoJogo(self):
		Tela.getTela(self).blit(Imagem.getFundoMenu(self), (0, 0))

	def desenhaInimigo(self, x, y):
		x_desenha = x
		y_desenha = y
		vetor = Inimigo.Inimigo(self)

		for i in vetor:
			for j in i:
				Tela.getTela(self).blit(j, (x_desenha, y_desenha))
				x_desenha += 100
			y_desenha += 50
			x_desenha = x

	def trajetoria(self):
		Nave.rect.top =	Nave.rect.top - Nave.getVelocidade(self)
	
	def desenhaTiro(self,x,y):
		Tela.getTela(self).blit(Nave.getTiro(self))
	