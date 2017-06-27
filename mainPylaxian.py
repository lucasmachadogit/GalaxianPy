import pygame
import sys
import random
from datetime import datetime
from pygame.locals import *
from TelaMenu import TelaMenu
from Creditos import Creditos
from Tela import Tela
from Audio import Audio
from TelaJogo import TelaJogo
from Jogo import Jogo
from Nave import Nave
from Tiro import Tiro
from GeraInimigo import GeraInimigo
from Status import Status
from BancoDeDados import BancoDeDados
from Pontuacao import Pontuacao

pygame.init()
relogio = pygame.time.Clock()
pygame.display.set_caption("Pylaxian")

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
	pause = None
	quantMunicao = 30
	jogou = False
	

	segundo = 0
	minuto = 0
	milisegundo = 0

	audio = Audio()
	tela = Tela()
	creditos = Creditos()
	telaMenu = TelaMenu()
	telaJogo = TelaJogo()
	jogo = Jogo()
	nave = Nave()
	tiro = Tiro(427, 0.88 * 600)
	teste = GeraInimigo()
	status = Status()
	pontuacao = Pontuacao()
	banco = BancoDeDados()

	audio.tocaMusicaFundo()

	now = datetime.now()
	dataHoje = str(now.day) + "/" + str(now.month) + "/" + str(now.year)	#Converte a data atual em string

	aux_pontos = 0
	aux_tempo = 0
	aux_data = dataHoje

	xNave, yNave = 400, (0.88 * 600)        
	xChange = 0

	rectNave = nave.nave.get_rect()
	
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
								menuEscolha = -1 #Escolhe sair
								break
		elif menuEscolha == 1:
			jogou = True

			tela.Fundo()
			jogo.fundoJogo()
			status.getPontos()
			status.getTempo()
			status.getMunicao()
			status.getPontua(pontos)
			status.getContaMunicao(quantMunicao)
			segundo, minuto, milisegundo = status.temporizador(milisegundo, segundo, minuto)

			rectNave.top = yNave
			rectNave.left = xNave
			rectNave.right = xNave + 32

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
						nave.disparar(xNave+16, 600 * 0.88)
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
						quantMunicao = 30
						pontos -= 5
						if pontos <= 0:
							menuEscolha = 4

					for x in nave.lista_disparo:
						if x_inimigo == 200:
							muda_xInimigo = -muda_xInimigo
						
						if x_inimigo == 10:
							muda_xInimigo = -muda_xInimigo
						
						if ini.rect.colliderect(x.rect):
							nave.lista_disparo.remove(x)
							teste.lista_inimigo.remove(ini)
							pontos += 15

					if ini.rect.colliderect(rectNave):
						audio.explosao()
						menuEscolha = 4
					
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
					if x.rect.top < -1: #Tiro some
						nave.lista_disparo.remove(x)

			tempo = str(minuto) + ":" + str(segundo) + ":" + str(milisegundo)	#Converte o tempo em string

			aux_pontos = pontos
			aux_data = dataHoje
			aux_tempo = tempo
		elif menuEscolha == 2:
			tela.Fundo()
			telaMenu.fundoMenu()
			pontuacao.blitaRanking()
			pontuacao.ranking()
			
			for evento in pygame.event.get():
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_v: 
						menuEscolha = 0
						break
		elif menuEscolha == 3:
			tela.Fundo()
			telaMenu.fundoMenu()
			creditos.Creditos()
			
			for evento in pygame.event.get():
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_v: 
						menuEscolha = 0
						break
		elif menuEscolha == 4:
			tela.Fundo()
			telaMenu.telaGameOver()
			status.statusGameOver()

			if len(teste.lista_inimigo) > 0:
				for ini in teste.lista_inimigo:
					teste.lista_inimigo.remove(ini)
			
			if len(nave.lista_disparo) > 0:
				for x in nave.lista_disparo:
					nave.lista_disparo.remove(x)
			
			quantMunicao = 30
			segundo = 0
			minuto = 0
			milisegundo = 0
			pontos = 0

			for evento in pygame.event.get():
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_s:
						menuEscolha = 0
						menu = 0
						break
		else:
			sairMenu = True

		pygame.display.update()

	if jogou == True:
		banco.salvarNoBanco(aux_data, aux_tempo, str(aux_pontos))

	banco.fechaCursor()
	banco.fechaBanco()
	
	pygame.quit()
	sys.exit()

main()