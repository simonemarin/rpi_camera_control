import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

coil_A_1_pin = [4,27]
coil_A_2_pin = [17,22]
coil_B_1_pin = [23,25]
coil_B_2_pin = [24,8]
 
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
 
def forward(delay, steps, motor):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0, motor)
    time.sleep(delay)
    setStep(0, 1, 1, 0, motor)
    time.sleep(delay)
    setStep(0, 1, 0, 1, motor)
    time.sleep(delay)
    setStep(1, 0, 0, 1, motor)
    time.sleep(delay)
  setStep(0, 0, 0, 0, motor)
 
def backwards(delay, steps, motor):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1, motor)
    time.sleep(delay)
    setStep(0, 1, 0, 1, motor)
    time.sleep(delay)
    setStep(0, 1, 1, 0, motor)
    time.sleep(delay)
    setStep(1, 0, 1, 0, motor)
    time.sleep(delay)
  setStep(0, 0, 0, 0, motor)
  
def setStep(w1, w2, w3, w4, motor):
  GPIO.output(coil_A_1_pin[motor], w1)
  GPIO.output(coil_A_2_pin[motor], w2)
  GPIO.output(coil_B_1_pin[motor], w3)
  GPIO.output(coil_B_2_pin[motor], w4)