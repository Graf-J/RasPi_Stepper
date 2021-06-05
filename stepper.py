import RPi.GPIO as GPIO
import time

class Stepper:
    
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
    
    def __init__(self):
        self.is_spinning = True
        
        self.__setup_pins()
        self.__setup_params()
        
    
    def __setup_pins(self):
        IN1 = 22
        IN2 = 23
        IN3 = 24
        IN4 = 25
        
        self.pins = [IN1, IN2, IN3, IN4]
        
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
            
            
    def __setup_params(self):
        self.acceleration_puffer = 32
        self.acceleration_repetition = 4
        
        
    def spin_forward(self, delay):
        self.__spin(Stepper.rotation_steps_forward, delay)
        
        
    def spin_backward(self, delay):
        self.__spin(Stepper.rotation_steps_backward, delay)
            
            
    def __spin(self, steps, delay):
        # Max Pace 0.0007, e.g. 0.5 would be much slower
        while self.is_spinning:
            for step in steps:
                ctr = 0
                for pin in self.pins:
                    GPIO.output(pin, step[ctr])
                    ctr += 1
                time.sleep(delay)
                
                
    def degrees(self, deg):
        if deg > 0:
            self.__spin_deg(Stepper.rotation_steps_forward, round((516/360) * deg))
        else:
            self.__spin_deg(Stepper.rotation_steps_backward, round( (516/360) * (deg * (-1)) ))
                
                
    def __spin_deg(self, steps, rotations):
        for _ in range(rotations):
            while self.is_spinning:
                for step in steps:
                    ctr = 0
                    for pin in self.pins:
                        GPIO.output(pin, step[ctr])
                        ctr += 1
                    time.sleep(0.0007)
                
        
    def stop(self):
        self.is_spinning = False
        
        
    def acc_forward(self):
        i = 1
        while self.spin:
            for step in Stepper.rotation_steps_forward:
                for _ in range(self.acceleration_repetition):
                    ctr = 0
                    for pin in self.pins:
                        GPIO.output(pin, step[ctr])
                        ctr += 1
                    time.sleep(0.00065)
            
                if i % self.acceleration_puffer == 0 and self.acceleration_repetition > 1:
                    self.acceleration_puffer += self.acceleration_puffer
                    self.acceleration_repetition -= 1
                
            i += 1
        
        
    # def slow(self):
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            