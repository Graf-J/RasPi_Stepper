import RPi.GPIO as GPIO
from threading import Thread
import time

class Stepper(Thread):
    rotation_steps_forward = [
      [1,0,0,0],
      [1,1,0,0],
      [0,1,0,0],
      [0,1,1,0],
      [0,0,1,0],
      [0,0,1,1],
      [0,0,0,1],
      [1,0,0,1]
    ]
    
    rotation_steps_backward = [
      [1,0,0,1],
      [0,0,0,1],
      [0,0,1,1],
      [0,0,1,0],
      [0,1,1,0],
      [0,1,0,0],
      [1,1,0,0],
      [1,0,0,0]
    ]
    
    SLOW = 0.002
    MEDIUM = 0.0016
    FAST = 0.0012
    TURBO = 0.0007
    
    def __init__(self, IN1, IN2, IN3, IN4):
        print('Constructor')
        Thread.__init__(self)
        self.__setup_pins([IN1, IN2, IN3, IN4])
        self.__setup_params()
        # self.deamon = True
        self.start()
        
    def __setup_pins(self, pins):
        print('Setup Pins')
        self.pins = pins
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
                
    def __setup_params(self):
        print('Setup Params')
        self.b_run = True
        self.is_spinning = False
        self.speed = Stepper.SLOW
        self.steps = Stepper.rotation_steps_forward
        
    def run(self):
        print('Run')
        while self.b_run:
            while self.is_spinning:
                for step in self.steps:
                    ctr = 0
                    for pin in self.pins:
                        GPIO.output(pin, step[ctr])
                        ctr += 1
                    time.sleep(self.speed)
            
    def forward(self, speed=0.002):
        print('Forward')
        self.is_spinning = True
        self.speed = speed
        self.steps = Stepper.rotation_steps_forward
    
    def backward(self, speed=0.002):
        print('Backward')
        self.is_spinning = True
        self.speed = speed
        self.steps = Stepper.rotation_steps_backward
        
    def increase_speed(self):
        print('Increase')
        if self.speed == Stepper.SLOW:
            self.speed = Stepper.MEDIUM
        elif self.speed == Stepper.MEDIUM:
            self.speed = Stepper.FAST
        elif self.speed == Stepper.FAST:
            self.speed = Stepper.TURBO
        elif self.speed == Stepper.TURBO:
            self.speed = Stepper.TURBO
        else:
            self.speed = Stepper.SLOW
    
    def decrease_speed(self):
        print('Decrease')
        if self.speed == Stepper.TURBO:
            self.speed = Stepper.FAST
        elif self.speed == Stepper.FAST:
            self.speed = Stepper.MEDIUM
        elif self.speed == Stepper.MEDIUM:
            self.speed = Stepper.SLOW
        elif self.speed == Stepper.SLOW:
            self.stop()
        else:
            self.speed = Stepper.SLOW
        
    def stop(self):
        print('Stop')
        self.is_spinning = False
        
    def terminate(self):
        print('Terminate')
        self.is_spinning = False
        self.b_run = False
            
    
        