#!/usr/bin/python
# encoding:latin1
import os, re, time

print ("Espere...")
resultado = open("resultado.txt", 'r')
print ("Resultado dos testes em cada um dos endereços: \% \n"+ resultado.read())

# Lendo o arquivo
enderecos = open("hosts.txt", 'r+')
hosts = [linha.strip() for linha in enderecos]

while True:
    for linha in hosts:
        linha.strip()
        comando = "ping -n 1 " + linha
        teste = "".join(os.popen(comando).readlines())
        resultado = open("resultado.txt", 'a+')
        if re.search('Received = 1', teste):
            resultado.write("O servidor "+linha+" no ar!\n")
        else:
            resultado.write("O servidor "+ linha +" fora do ar !\n")
        print(resultado.read())

    resultado.close()
    print("Final!")
    print("Espere 60 segundos.")
    time.sleep(60)




