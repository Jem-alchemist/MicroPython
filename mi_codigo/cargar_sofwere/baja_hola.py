# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Cargar lista.py en memoria lo graba como fichero y ejecuta el fichero.

import urequests
url_base ='https://raw.githubusercontent.com/Jem-alchemist/MicroPython/master/mi_codigo/cargar_sofwere/'
r = urequests.get(url_base + 'lista.py')
f = open('lista.py', 'w')
f.write(r.text)
f.close()
exec(open('lista.py').read())
