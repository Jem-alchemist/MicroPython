# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Cargar lista.py en memoria de bichoo y lo ejecuta.

import urequests
url_base ='https://raw.githubusercontent.com/Jem-alchemist/MicroPython/mi_codigo/cargar_sofwere/master/'
r = urequests.get(url_base + 'lista.py')
exec (r.text)

