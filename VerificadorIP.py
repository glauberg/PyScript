#!/usr/bin/python3

import os, re

print ("Verificando conexao...")
ip = input ("Digite o IP:")
cmd = "ping " + ip
r = "".join(os.popen(cmd).readlines())
print (r)

if re.search ("Recebidos", r):
  print ("Link Ativo")
else:
  print ("Link Inativo")
	

 
