import network
import usocket as socket
from machine import I2C, Pin
from imu import MPU6050
i2c = I2C(scl=Pin(0), sda=Pin(2))
mpu6050 = MPU6050(i2c)
accel = mpu6050.accel
gyro = mpu6050.gyro
print(accel.xyz)
print(gyro.xyz)
print(mpu6050.temperature)

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.ifconfig(('192.168.0.124', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando la red...')
        wlan.connect('Gallina','Uno2Tres')
        while not wlan.isconnected():
            pass
    print('Configuracion de la red:', wlan.ifconfig())
do_connect()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pin_out = machine.Pin(2, machine.Pin.OUT)
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
    elif comando[0:5] == "ledon":
      print("Comando ledon")
      conn.send("Led encendido" + "\n")
      pin_out.off()
    elif comando[0:5] == "ledof":
      print("Comando ledoff")
      conn.send("Led apagado" + "\n")
      pin_out.on()
    elif comando[0:5] == "ejecu":
      print("Comando ejecutar")
      exec(comando.split(':')[1])
    else:
      print("Envio un comando no reconocido")
      conn.send("Comando no contemplado" + "\n")
    conn.close()
  except:
    print("Error")
    print("Error en la comunicacion")
conn.close()
s.close()
  

