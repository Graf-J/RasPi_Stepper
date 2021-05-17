import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_pins = [22, 23, 24, 25]

for pin in GPIO_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  
rotation_steps = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

for i in range(512):
    for step in rotation_steps:
        ctr = 0
        for pin in GPIO_pins:
            GPIO.output(pin, step[ctr])
            ctr += 1
        time.sleep(0.0008)

GPIO.cleanup()
