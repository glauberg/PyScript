#!/usr/bin/python
#decoding: latin1

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
operacao = raw_input("Digite a operação: [S]oma S[U]btração [D]ivisão [M]ultiplicação: ")

operacao = operacao.upper()
if operacao == 'S':
   resultado = valor1 + valor2
   print "O resultado da operação de SOMA é: " + str(resultado)

elif operacao == 'U':
   resultado = valor1 - valor2
   print "O resultado da operação de SUBTRAÇÃO é: " + str(resultado)

elif operacao == 'M':
   resultado = valor1 * valor2
   print "O resultado da operação de MULTIPLICAÇÃO é: " + str(resultado)

elif operacao == 'D':
   try:
     resultado = valor1 / valor2
   
   except:
     print "## ERRO! Divisão por ZERO ###"
     resultado = 0          
   
   print "O resultado da operação de DIVISÃO é: " + str(resultado)

else:
   print '### Operação Inválida ###'




