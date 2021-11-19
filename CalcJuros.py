#!/usr/bin/python
# decoding: latin1
# Calcular juros a partir de um valor

def calcula(a,b,c):
    juros_dia = (c/30)/100
    valor_juros = a * (juros_dia * b)
    valor_atual = a + valor_juros
    return valor_atual

# Recebe dados do teclado
valorC = float(input("Digite o valor da compra: "))
diasV = int(input("Digite os dias vencidos: "))
txJuros = float(input("Digite a taxa de juros mensal: "))

# Chamda da função
print calcula(valorC, diasV, txJuros)


