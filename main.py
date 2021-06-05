import RPi.GPIO as GPIO
from threading import Thread
import time
from stepper import Stepper


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    
def main():
    stepper = Stepper()
    t = Thread(target=stepper.degrees, args=(540,))
    t.start()
    time.sleep(1)
    stepper.stop()
    
    
def cleanup():
    print('Cleanup')
    GPIO.cleanup()
    

if __name__ == '__main__':
    setup()
    main()
    # cleanup()
