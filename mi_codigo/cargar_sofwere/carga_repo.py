# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Cargar lista.py en memoria de bichoo y lo ejecuta.

import urequests
url_base ='https://raw.githubusercontent.com/Jem-alchemist/MicroPython/master/mi_codigo/cargar_sofwere/'
r = urequests.get(url_base + 'lista.py')
exec (r.text)

