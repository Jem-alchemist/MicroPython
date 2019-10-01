# Jesus Manuel Escobar Muñoz
# 29 de Septiembre de 2019
# Ejemplo para cargar en el bicho
import gc 
import os
import sys
import machine
import esp
import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
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
titulo="\nDatos de memoria"
print(titulo)
print("-" * len(titulo))                                                                
print("Memoria RAM disponible:" + str(gc.mem_free()/1024) + "Kbytes")
print("Memoria flash:" + str(esp.flash_size ()/1024) + "Kbytes")
print ("Memoria flash del usuario:" + str(esp.flash_user_start()/1024) + "Kbytes")
titulo="\nDatos de red"
print(titulo)
print("-" * len(titulo))
if sta_if.active():
  print ("Wifi activa:" + sta_if.ifconfig()[0])
  print("Mac:" + str(sta_if.config('mac')))
  if sta_if.isconnected():
    print("Conectada")
    print("Essid:" + sta_if.config('essid'))
  else:
    print("Desconectada")
else:
  print ("Wifi inactiva")
if ap_if.active():
  print ("Punto de acceso activo:" + ap_if.ifconfig()[0])
  print("Essid:" + ap_if.config('essid'))
  print("Mac:" + str(ap_if.config('mac')))
  if ap_if.isconnected():
    print("Conectado")
  else:
    print("Desconectado")
else:
  print ("Punto de acceso inactivo")
#print("Para configurar tu AP: ap_if.config(essid='tu_essid',password='tu_password'")
#print("siendo ap_if = network.WLAN(network.AP_IF) *pon una password de al menos 8 caracteres")
titulo="\nListamos los ficheros"
print(titulo)
print("-" * len(titulo))
for fichero in os.listdir():
  print(fichero)

                                                                  
gc.collect()                                                                
gc.mem_free() 
