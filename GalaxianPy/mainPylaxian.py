import pygame
import sys
import time
from pygame.locals import *
from TelaMenu import TelaMenu
from Creditos import Creditos
from Tela import Tela
from Audio import Audio
from TelaJogo import TelaJogo
from Jogo import Jogo
from Nave import Nave

pygame.init()
relogio = pygame.time.Clock()
pygame.display.set_caption("Pylaxian")

def main():
	
	menu = 0 
	menuEscolha = 0
	menuJogo = 0
	sairMenu = False
	escolheJogar = False
	x_inimigo = 50
	y_inimigo = 50
	muda_xInimigo = 0.5
	muda_yInimigo = 0.1

	audio = Audio()
	tela = Tela()
	creditos = Creditos()
	telaMenu = TelaMenu()
	telaJogo = TelaJogo()
	jogo = Jogo()
	nave = Nave()
	audio.tocaMusicaFundo()

	xNave,yNave = 400, (0.88 * 600)        
	xChange = 0
	yTiro =  (0.88 * 600) - 2  
	controle = False
	while not sairMenu:
		relogio.tick(60)
		if menuEscolha == 0:
			tela.Fundo()
			telaMenu.fundoMenu()
			telaMenu.MenuSeleciona(menu)
			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
				elif evento.type == pygame.KEYDOWN:
					if menuEscolha == 0:
						if evento.key == pygame.K_DOWN: 
							audio.tocaEfeito()
							if menu < 3:  
								menu = menu + 1
							else:
								menu = 0	
						elif evento.key == pygame.K_UP:
							audio.tocaEfeito()
							if menu > 0:
								menu = menu - 1	
							else:
								menu = 3 
						elif evento.key == pygame.K_SPACE:
							if menu == 0:
								menuEscolha = 1 #Escolhe jogar
								break
							elif menu == 1:
								menuEscolha = 2 #Escolhe pontuação
								break
							elif menu == 2: 
								menuEscolha = 3 #Escolhe créditos
								break
							else:
								menuEscolha = 4 #Escolhe sair
								break
		elif menuEscolha == 1:
			tela.Fundo()
			jogo.fundoJogo()
			jogo.desenhaInimigo(x_inimigo, y_inimigo)
			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_LEFT: 
						xChange = -nave.getVelocidade()	
					elif evento.key == pygame.K_RIGHT:
						xChange = nave.getVelocidade()
					elif evento.key == pygame.K_SPACE:
						controle = True
				if evento.type == KEYUP:
					if evento.key == pygame.K_LEFT: 
						xChange = 0
					if evento.key == pygame.K_RIGHT:
						xChange = 0    
			if xNave < 3:
				xNave = 3
			elif xNave > 800 - 67:
				xNave =  800 - 67
			else:
				xNave += xChange
			
			x_inimigo += muda_xInimigo
			y_inimigo += muda_yInimigo
			yTiro -= 1 
			if x_inimigo == 200:
				muda_xInimigo = -muda_xInimigo

			if x_inimigo == 10:
				muda_xInimigo = -muda_xInimigo
			if controle:
				jogo.desenhaTiro(xNave + 28,yTiro)
			jogo.movimentaNave(xNave,yNave)
		elif menuEscolha == 2:
			tela.Fundo()
		elif menuEscolha == 3:
			tela.Fundo()
			telaMenu.fundoMenu()
			creditos.Creditos()
			for evento in pygame.event.get():
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_v: 
						menuEscolha = 0
						break	
		else:
			sairMenu = True
		
		pygame.display.update()
main()
pygame.quit()
sys.exit()
