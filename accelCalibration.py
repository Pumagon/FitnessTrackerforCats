from machine import I2C, Pin
from micropython_bmi160 import bmi160
import time

i2c = I2C(0, scl=Pin(17), sda=Pin(16))
bmi = bmi160.BMI160(i2c)

accel = bmi.acceleration

print("Accel:", accel)

# Put BMI160 sensor on a flat surface for calibration
calibration_samples = 1000
accel_bias = [0, 0, 0]

#time.sleep(10)

for _ in range(calibration_samples):
    accel = bmi.acceleration
    accel_bias[0] += accel[0]
    accel_bias[1] += accel[1]
    accel_bias[2] += accel[2]

accel_bias = [x / calibration_samples for x in accel_bias]

# Removing gravitational acceleration effect
#accel_bias[2] -= 16384  # 16384 LSB = 1g

print("Accel Bias:", accel_bias)
print("Sum: ", accel_bias[0] + accel_bias[1] + accel_bias[2])
