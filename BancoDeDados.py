import sqlite3

class BancoDeDados(object):
	def __init__(self):
		self.__banco = sqlite3.connect('pontuacaoDB.db')
		self.__cursor = self.__banco.cursor()

		self.__cursor.execute('create table if not exists PONTUACAO(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, data Text, '\
		'tempo Text, pontos Text)')

	def salvarNoBanco(self, data, tempo, pontos):
		self.__cursor.execute("insert into PONTUACAO (data, tempo, pontos) values (?, ?, ?)", (data, tempo, pontos))
		self.__banco.commit()	#Salva no banco de dados
		#self.__cursor.close()	#Fecha o cursor
		#self.__banco.close()	#Fecha a conexão com o banco de dados

	