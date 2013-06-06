#!/usr/bin/python
import subprocess
from time import sleep

ARQUIVO = "resultado.txt"
print "Aguarde"
print "Resultados dos testes em cada um dos enderecos: "
while True:
	logfile = open(ARQUIVO, "a")
	servidores = open("servidores", "r")
	for ip in servidores:
		ips = ip.strip()
		command = 'ping -q -c1 ' + ips + ' | fgrep received | cut -d " " -f 4'.format(ips)
		output = subprocess.check_output(command, shell=True)
		if output.strip() == "1":
			logfile.write("O servidor " + ips + " esta ativo.\n")
		else:
			logfile.write("O Servidor " + ips + " nao responde.\n")
		print "."
	logfile.write("\n")
	logfile.close()
	servidores.close()
	print "Terminou!"
	print "Aguarde 60 segundos"
	sleep(60)
