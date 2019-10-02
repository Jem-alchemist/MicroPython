# Jesus Manuel Escobar Muñoz
# 30 de Septiembre de 2019
# Ejemplo de un servidor conectado a un modulo TM1638

import usocket as socket
import tm1638
from time import sleep_ms
import machine
import dht
d = dht.DHT22(machine.Pin(16))
adc = machine.ADC(0)
tm = tm1638.TM1638(stb=machine.Pin(13), clk=machine.Pin(14), dio=machine.Pin(12))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 11000))
s.listen(5)
while True:
  try:
    conn, addr = s.accept()
    print('Nueva conexion %s' % str(addr))
    request = conn.recv(1024)
    comando = str(request, 'utf-8')
    if comando[0:5] == "final":
      print("Comando fianl")
      conn.send("Final del proceso" + "\n")
      break
    elif comando[0:3] == "luz":
      l = adc.read()
      tm.clear()
      tm.show('L-' + str(l))
      conn.send("Luminosidad:" + str(l) + "\n")
    elif comando[0:11] == "temperatura":  
      d.measure()
      t = d.temperature()
      tm.clear()
      tm.show('t-' + str(t))
      conn.send("Temperatura:" + str(t) + "\n")
    elif comando[0:7] == "humedad":
      d.measure()
      h = d.humidity()
      tm.clear()
      tm.show('h-' + str(h))
      conn.send("Humedad:" + str(h) + "\n")
    elif comando[0:4] == "leds":
      tm.clear()
      tm.leds(int(comando[5:8]))
      conn.send(comando + " ejecutado\n")
    else:
      print("Envio un comando no reconocido")
      conn.send("Comando:" + comando + " comando no contemplado" + "\n")
    conn.close()
  except:
    print("Error")
conn.close()
s.close()
