# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Ejemplo de un simple servidor


import usocket as socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

web_primera = """<html><head> <title>Servidor Jem</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <body> <p><a href="/?segunda"><img src="https://i0.wp.com/radiotgw.gob.gt/wp-content/uploads/2018/11/Elefante.jpg?resize=850%2C425&amp;ssl=1" alt="elefante" width="850" height="425" /></a></p>
<p>&nbsp;</p></body></html>"""
  
web_segunda = """<html><head> <title>Servidor Jem</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <body> <p><a href="/?primera"><img src="https://static.abc.es/media/sociedad/2016/09/25/elefante-africano-kz7G--620x349@abc.jpg" alt="elefante" width="850" height="425" /></a></p>
<p>&nbsp;</p></body></html>"""

web_entrada ="""<html><head> <title>Servidor Jem</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <body> <p><a href="/?primera"><img style="display: block; margin-left: auto; margin-right: auto;" src="https://static.abc.es/media/sociedad/2016/09/25/elefante-africano-kz7G--620x349@abc.jpg" alt="elefante" width="850" height="425" /></a></p>
<p>&nbsp;</p></body></html>"""

while True:
 # try:
    conn, addr = s.accept()
    print('Nueva conexion %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    primera = request.find('/?primera')
    segunda = request.find('/?segunda')
    if primera == 6:
      print('primera')
      response = web_primera
    elif segunda == 6:
      print('segunda')
      response = web_segunda
    else:
      print('primera')
      response = web_entrada
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  #except:
   # print("Error")
s.close()
