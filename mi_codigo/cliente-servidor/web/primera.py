def resultado(datos_entrada):
  datos = datos_entrada.split(',')
  dentrada = []
  dentrada.append(len(datos))
  for dato in datos:
    if dato == "": 
      dentrada[0] = 0
      break
    dentrada.append(dato)
  print('Numero de datos:' + str(dentrada[0]))
  numero=0
  for dato in dentrada:
    if numero > 0: print('Dato' + str(numero) + ":" + str(dato))
    numero += 1
  html = """<html><head> <title>Servidor Jem</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <body> <p><a href="/segunda.py"><img src="https://i0.wp.com/radiotgw.gob.gt/wp-content/uploads/2018/11/Elefante.jpg?resize=850%2C425&amp;ssl=1" alt="elefante" width="850" height="425" /></a></p>
<p>&nbsp;</p></body></html>"""
  return html
