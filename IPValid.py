#!/usr/bin/python
# encoding: latin1
f=open("./listaip.txt","r")
lista = f.readlines()
f.close()
ipvalido = ""
ipnaovalido = ""
for i in range (len(lista)):
    	lista2 = lista[i].rsplit(".")
	if (int(lista2[0]) <= 255 and int(lista2[1]) <= 255 and int(lista2[2]) <= 255 and int(lista2[3]) <= 255):
        	ipvalido += lista[i] + "\n"
    	else:
        	ipnaovalido += lista[i] + "\n"
f=open("./ipvalido.txt","w")
f.write(ipvalido)
f.close()
f=open("./ipnaovalido.txt","w")
f.write(ipnaovalido)
f.close()
print ("arquivos gerados com sucesso!")
