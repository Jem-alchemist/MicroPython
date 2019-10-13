def resultado(datos_entrada):
  import os
  ficheros = os.listdir()
  html = '<html><head><title>Servidor Jem</title><meta name="viewport" content="width=device-width, initial-scale=1"><body>'
  for fichero in ficheros: 
    html += '<p style="text-align: center;"><a href="' + fichero + '" target="_blank" rel="noopener">' + fichero + '</a></p>'
  html += '</body></html>'
  return html
