# Jesus Manuel Escobar Muñoz
# 10 de Octubre de 2019
# Ejemplo de un servidor web


import usocket as socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  #try:
    conn, addr = s.accept()
    print('Nueva conexion %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    pagina = request.split(' ')[1][1:]
    if pagina == "parar_bucle": break
    datos = pagina.find('?')
    dato = ""
    if datos != -1:
      dato = pagina[datos+1:]
      pagina = pagina[:datos]
    try:
      print('pagina:'+pagina +'dato:'+dato)
      exec(open(pagina).read())
      response = resultado(dato)
      #print('sin error de apertuta response = ' +response)
    except:
      response = open('index.html').read()
      #print('error de apertura response = ' + response)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.sendll(response)
    conn.send('Connection: close\n\n')
    conn.close()
  #except:
   # print("Error")
s.close()
