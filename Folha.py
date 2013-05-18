#!/usr/bin/python
# encoding: latin1
# Inclusão de funcionários e salários
# Autor: Prof. Glauber Galvão
#
def Inclusao():
	folha = open("funcionario.txt",'a')
	while True:
		nome = raw_input("Digite o nome do funcionário: ")
		salario = float(input("Digite o salário: "))
		folha.write(nome + "," + str(salario) + "\n")
		sair = raw_input("Cadastrar +funcionários(S/N)? ")
		sair = sair.upper()
		if (sair == "N"):
			folha.close()
			Menu()

def CalculaINSS():
	# Abrindo arquivo
	folha = open("funcionario.txt",'r')
	linha = folha.readlines()
	folha.close()
	inss = open("descontos.txt",'w')
	for i in range (len(linha)):
		linha2 = linha[i].rsplit(",")
		nome = linha2[0]
		salario = float(linha2[1])
	
		if (salario >= 670.00) & (salario <= 799.99):
		   vinss = salario * 0.08
		   inss.write(nome+","+str(salario)+","+str(vinss)+"\n")
		elif (salario >= 800.00) & (salario <= 1199.99):
		   vinss = salario * 0.11
		   inss.write(nome+","+str(salario)+","+str(vinss)+"\n")
		elif salario >= 1200.00:
		   vinss = salario * 0.15
		   inss.write(nome+","+str(salario)+","+str(vinss)+"\n")			
			
	inss.close()
	Menu()
	
def Menu():
	while True:
		print "Folha de Pagamento"
		print "O que você deseja?"
		print "(1) Inclusão de funcionários"
		print "(2) Cálculo de INSS"
		print "(3) Sair"
		opcao = int(input("Digite sua opção: "))
	
		if (opcao == 1):
			Inclusao()
		elif (opcao == 2):
			CalculaINSS()
		else:
			raise SystemExit

# Início do programa	
Menu()
