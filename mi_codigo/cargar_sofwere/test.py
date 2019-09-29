# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Ejemplo para cargar en el bicho
import gc 
import os
import sys
import machine
import esp
titulo="Informacion general del microcontrolador"
print(titulo)
print("-" * len(titulo) +"\n")
titulo="Datos del sistema"
print(titulo)
print("-" * len(titulo))
print("Nombre del sistema:" + os.uname().sysname)
print("Nombre del nodo:" + os.uname().nodename)
print("Lanzamiento:" + os.uname().release)
print("version:" + os.uname().version)
print("Maquina:" + os.uname().machine)
print("Frecuencia de relog del procesador:" + str(machine.freq()/1000000) + "MHz")
gc.collect()
titulo="Datos de memoria"
print(titulo)
print("\n" + "-" * len(titulo))                                                                
print("Memoria RAM disponible:" + str(gc.mem_free()/1024) + "Kbytes")
print("Memoria flash:" + str(esp.flash_size ()/1024) + "Kbytes")
print ("Memoria flash del usuario:" + str(esp.flash_user_start()/1024) + "Kbytes")
titulo="Listamos los ficheros"
print(titulo)
print("\n" + "-" * len(titulo))
for fichero in os.listdir():
  print(fichero)

                                                                  
gc.collect()                                                                
gc.mem_free() 
