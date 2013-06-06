#!/usr/bin/python
#-*- encoding: latin1 -*-

# Função Média
def media(n1,n2,n3):
	m = (n1+n2+n3) / 3
	return m

def situacao(med):
	if med >= 7:
		print ("Aluno APROVADO")
	else:
		print ("Aluno REPROVADO")

# Entrada de dados
aluno=raw_input("digite o nome do aluno: ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

# Chamada da função
print (aluno, media(nota1, nota2, nota3))
situacao(media(nota1,nota2,nota3))
