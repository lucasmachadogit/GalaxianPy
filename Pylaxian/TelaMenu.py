import pygame
from pygame.locals import *
from Tela import Tela
from Imagem import Imagem

pygame.init()

class TelaMenu(Tela, Imagem):
    def __init__(self):
        Tela.__init__(self)
        Imagem.__init__(self)

        try:
            self.__fonte_titulo = pygame.font.Font("PressStart2P.ttf", 50)
            self.__fonte_menu = pygame.font.Font("PressStart2P.ttf", 25)
            self.__fonte_texto = pygame.font.Font("PressStart2P.ttf", 15)
        except IOError:
            print("Não foi possível carregar fonte do jogo!!")
			
        self.__titulo = self.__fonte_titulo.render("Pylaxian", True, Tela.getCorObjeto(self))
        self.__player = self.__fonte_menu.render("Jogar", True, Tela.getCorObjeto(self))
        self.__pontuacao = self.__fonte_menu.render("Pontuação",True,Tela.getCorObjeto(self))
        self.__creditos = self.__fonte_menu.render("Créditos", True, Tela.getCorObjeto(self))
        self.__sair = self.__fonte_menu.render("Sair", True, Tela.getCorObjeto(self))
        self.__instrucao_menu = self.__fonte_texto.render("Pressione ESPAÇO para escolher a opção", True, Tela.getCorObjeto(self))

    def fundoMenu(self):
        Tela.getTela(self).blit(Imagem.getFundoMenu(self), (0, 0))
	
    def MenuSeleciona(self, seleciona):
        if seleciona == 0:
            pygame.draw.rect(Tela.getTela(self), Tela.getCorClaro(self), (110,200,300,30))
        elif seleciona == 1:
            pygame.draw.rect(Tela.getTela(self),Tela.getCorClaro(self), (110,230,300,30))
        elif seleciona == 2:
            pygame.draw.rect(Tela.getTela(self), Tela.getCorClaro(self), (110,260,300, 30))
        elif seleciona == 3:
            pygame.draw.rect(Tela.getTela(self), Tela.getCorClaro(self), (110,290,300, 30))
				
        Tela.getTela(self).blit(self.__titulo, (200, 50))
        Tela.getTela(self).blit(self.__player, (120, 200))
        Tela.getTela(self).blit(self.__pontuacao,(120,230))
        Tela.getTela(self).blit(self.__creditos, (120, 260))
        Tela.getTela(self).blit(self.__sair, (120, 290))
        Tela.getTela(self).blit(self.__instrucao_menu, (120, 550))

    def telaGameOver(self):
        Tela.getTela(self).blit(Imagem.getGameOver(self), (0, 0))
