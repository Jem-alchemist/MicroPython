# Jesus Manuel Escoabr Muñoz
# 29 de septiembre de 2019
# Prueba del giroscoppio MPU6050

from machine import I2C, Pin
from imu import MPU6050
i2c = I2C(scl=Pin(0), sda=Pin(2))
mpu6050 = MPU6050(i2c)
accel = mpu6050.accel
gyro = mpu6050.gyro
print(accel.xyz)
print(gyro.xyz)
print(mpu6050.temperature)
# En el bucle sigiente te da la posicion x,y en grados
while 1:
  print('X:' + str(mpu6050.accel.xyz[0]*90)) + '\nY:' + str(mpu6050.accel.xyz[1]*90)))
