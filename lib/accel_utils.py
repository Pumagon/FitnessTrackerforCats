from machine import Pin, I2C
from micropython_bmi160 import bmi160

class Accelerometer:
    def __init__ (self, i2cChannel, sda, scl):
        # BMI160 setup
        sda = Pin(sda)
        scl = Pin(scl)
        i2c = I2C(i2cChannel, sda=sda, scl=scl)
        
        self.bmi = bmi160.BMI160(i2c)
        self.alpha = 0.9
        self.prevAccel = [0.0, 0.0, 0.0]
        self.prevFilteredAccel = [0.0, 0.0, 0.0]
        self.currentFilteredAccel = [0.0, 0.0, 0.0]

    # Get Corrected Acceleration data
    def get_corrected_accel(self):
        currentAccel = self.bmi.acceleration
        for i in range(3):
            self.currentFilteredAccel[i] = \
                self.alpha * (self.prevFilteredAccel[i] + (currentAccel[i] - self.prevAccel[i]))
            self.prevAccel[i] = currentAccel[i]
            self.prevFilteredAccel[i] = self.currentFilteredAccel[i]

        return self.currentFilteredAccel

    # Calculate Activity Value
    def calculateActivity(self):
        accel = self.get_corrected_accel()
        activityValue = sum(abs(value) for value in accel)
        
        return activityValue
