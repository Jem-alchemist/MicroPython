# Jesus Manuel Escobar Muñoz
# 10 de Octubre de 2019
# Ejemplo de un servidor web


import usocket as socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    conn, addr = s.accept()
    print('Nueva conexion %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    pagina = request.split(' ')[1][1:]
    if pagina == "parar_bucle": break
    try:
      exec(open(pagina).read())
      response = resultado()
      print('sin error de apertuta response = ' +response)
    except:
      print('error de apertura response = ' + response)
      response = open('index.html').read()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except:
    print("Error")
s.close()
