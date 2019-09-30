# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Ejemplo de un simple cliente

import usocket as socket

def cliente(ip,puerto,comando)
  s = socket.socket()
  ai = socket.getaddrinfo(ip, puerto)
  print("Informacion de la direccion:", ai)
  addr = ai[0][-1]
  print("Conectando a la direccion:", addr)
  s.connect(addr)
  s.send(comando+"\n")
  print(s.recv(4096))
  s.close()
