import pygame
from pygame.locals import *
from Nave import Nave
from Tela import Tela
from Imagem import Imagem

pygame.init()

class Jogo(Nave, Tela, Imagem):
	def __init__(self):
		Nave.__init__(self)
		Tela.__init__(self)
		Imagem.__init__(self)
		
	def movimentaNave(self,x,y):
		Tela.getTela(self).blit(Nave.getNave(self), (x,y))
	
	def fundoJogo(self):
		Tela.getTela(self).blit(Imagem.getFundoMenu(self), (0, 0))
