import sqlite3

class BancoDeDados(object):
	def __init__(self):
		self.banco = sqlite3.connect('pontuacaoDB.db')
		self.cursor = self.banco.cursor()

		try:
			self.cursor.execute('create table if not exists PONTUACAO(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, data Text, '\
			'tempo Text, pontos Integer)')
		except:
			print("Erro ao construir banco de dados!!")

		self.__placar = []

	def salvarNoBanco(self, data, tempo, pontos):
		self.cursor.execute("insert into PONTUACAO (data, tempo, pontos) values (?, ?, ?)", (data, tempo, pontos))
		self.banco.commit()	#Salva no banco de dados

	def fechaCursor(self):
		self.cursor.close()

	def fechaBanco(self):
		self.banco.close()

	def getCursor(self):
		return self.cursor

	def buscaNoBanco(self):		
		self.cursor.execute("select * from PONTUACAO order by pontos desc")

		for i in self.cursor.fetchall():
			self.__placar.append(i)

	def getPlacar(self):
		return self.__placar
	