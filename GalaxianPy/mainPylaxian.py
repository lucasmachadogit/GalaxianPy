import pygame
import sys
import random
from pygame.locals import *
from TelaMenu import TelaMenu
from Creditos import Creditos
from Tela import Tela
from Audio import Audio
from TelaJogo import TelaJogo
from Jogo import Jogo
from Nave import Nave
from Tiro import Tiro
from Teste import Teste
from Status import Status


pygame.init()
relogio = pygame.time.Clock()
pygame.display.set_caption("Pylaxian")

def doRectsOverLap(rect1, rect2):
	for a, b in [(rect1,rect2),(rect2, rect1)] :
		if((isPointInsideRect(a.left,a.top,b)) or (isPointInsideRect(a.left,a.bottom, b)) or (isPointInsideRect(a.right,a.top,b)) or (isPointInsideRect(a.right,a.bottom,b))):
			return True
	return False 

def isPointInsideRect(x,y,rect):
	if x > rect.left and x < rect.right and y > rect.top and y < rect.bottom:
		return True
	else:
		return False  

def main():
	
	menu = 0 
	menuEscolha = 0
	menuJogo = 0
	sairMenu = False
	escolheJogar = False
	x_inimigo = 100
	y_inimigo = 100
	muda_xInimigo = 0.5
	muda_yInimigo = 0.1
	pontos = 0
	quantMunicao = 80

	audio = Audio()
	tela = Tela()
	creditos = Creditos()
	telaMenu = TelaMenu()
	telaJogo = TelaJogo()
	jogo = Jogo()
	nave = Nave()
	tiro = Tiro(427, 0.88 * 600)
	teste = Teste()
	status = Status()

	audio.tocaMusicaFundo()

	xNave, yNave = 400, (0.88 * 600)        
	xChange = 0

	
	def geraInimigos(x, y):
		x_pos = x
		y_pos = y
		for i in range(4):
			for j in range(6):
				teste.gerarInimigo(x_pos ,y_pos)	
				x_pos = x_pos + 40
			y_pos = y_pos + 40
			x_pos = x  
	
	geraInimigos(x_inimigo, y_inimigo)

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
			status.getPontos()
			status.getTempo()
			status.getMunicao()
			status.getPontua(pontos)
			status.getContaMunicao(quantMunicao)

			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
				
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_LEFT: 
						xChange = -nave.getVelocidade()	
					elif evento.key == pygame.K_RIGHT:
						xChange = nave.getVelocidade()
					
					if evento.key == pygame.K_SPACE:
						nave.disparar(xNave+27, 600 * 0.88)
						audio.getTiroNave()
						quantMunicao -= 1
				
				if evento.type == KEYUP:
					if evento.key == pygame.K_LEFT: 
						xChange = 0
					if evento.key == pygame.K_RIGHT:
						xChange = 0

			if len(teste.lista_inimigo) > 0:
				for ini in teste.lista_inimigo:
					ini.desenha()
					ini.trajetoriaInimigo()
					
					if ini.rect.top > 600:
						teste.lista_inimigo.remove(ini)

					for x in nave.lista_disparo:
						if x_inimigo == 200:
							muda_xInimigo = -muda_xInimigo
						
						if x_inimigo == 10:
							muda_xInimigo = -muda_xInimigo
						
						if doRectsOverLap(ini.rect, x.rect):
							nave.lista_disparo.remove(x)
							teste.lista_inimigo.remove(ini)
							pontos += 10
						
			else:
				geraInimigos(random.randint(10, 350), 10)

			x_inimigo += muda_xInimigo 
			x_inimigo += muda_yInimigo	
			
			if xNave < 3:
				xNave = 3
			elif xNave > 800 - 67:
				xNave =  800 - 67
			else:
				xNave += xChange
		
			jogo.movimentaNave(xNave, yNave)

			if len(nave.lista_disparo) > 0:
				for x in nave.lista_disparo:
					x.desenhaTiro()
					x.trajetoria()
					if x.rect.top < -10: #Tiro some
						nave.lista_disparo.remove(x)
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
	
	pygame.quit()
	sys.exit()

main()