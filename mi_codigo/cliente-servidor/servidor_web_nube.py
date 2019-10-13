# Jesus Manuel Escobar Muñoz
# 10 de Octubre de 2019
# Ejemplo de un servidor web

import urequests
import usocket as socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
url_base ='https://raw.githubusercontent.com/Jem-alchemist/MicroPython/master/mi_codigo/cliente-servidor/web/'
while True:
  try:
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
      print('pagina:'+ pagina + 'dato:'+dato)
      r = urequests.get(url_base + pagina)
      if pagina.find('.py') != -1:
        exec(r.text)
        response = resultado(dato)
      else:# pagina.find('.html') != -1:
        response = r.text
      #print('sin error de apertuta response = ' +response)
      #else:
       # response = 'no comtemplado'
    except:
      #response = open('index.html').read()
      print('error de apertura response = ' + response)
      response = 'error de apertura response = ' + response
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except:
    print("Error")
s.close()
