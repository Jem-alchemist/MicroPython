# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Ejemplo de un simple servidor en puerto 80


import usocket as socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
  try:
    conn, addr = s.accept()
    print('Nueva conexion %s' % str(addr))
    request = conn.recv(1024)
    comando = str(request, 'utf-8')
    if comando[0:5] == "final":
      print("Comando fianl")
      conn.send("Final del proceso" + "\n")
      break
    elif comando[0:5] == "ledon":
      print("Comando ledon")
      conn.send("Led encendido" + "\n")
      pin_out.off()
    elif comando[0:5] == "ledof":
      print("Comando ledoff")
      conn.send("Led apagado" + "\n")
      pin_out.on()
    else:
      print("Envio un comando no reconocido")
      conn.send(comando + "Comando no contemplado" + "\n")
    conn.close()
  except:
    print("Error")
conn.close()
s.close()
