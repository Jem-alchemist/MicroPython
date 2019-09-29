#https://forum.micropython.org/viewtopic.php?f=16&t=6260&start=20

from machine import I2C, Pin
from imu import MPU6050
i2c = I2C(scl=Pin(0), sda=Pin(2))
mpu6050 = MPU6050(i2c)
accel = mpu6050.accel
gyro = mpu6050.gyro
print(accel.xyz)
print(gyro.xyz)
print(mpu6050.temperature)


print('X:' + str(mpu6050.accel.xyz[0]) + '\nY:' + str(mpu6050.accel.xyz[1]))
print('X:' + str(mpu6050.accel.xyz[0]*90)) + '\nY:' + str(mpu6050.accel.xyz[1]*90)))
