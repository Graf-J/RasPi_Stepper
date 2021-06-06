import RPi.GPIO as GPIO
from threading import Thread
import time
from stepper import Stepper


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
def user_interaction(stepper):
    i = input("""
    1) Forward
    2) Backward
    3) Slow
    4) Increase
    5) Decrease
    6) Stop
    7) Terminate
    """)
    
    if int(i) == 1:
        stepper.forward()
    elif int(i) == 2:
        stepper.backward()
    elif int(i) == 3:
        stepper.slow(1)
    elif int(i) == 4:
        stepper.increase_speed()
    elif int(i) == 5:
        stepper.decrease_speed()
    elif int(i) == 6:
        stepper.stop()
    elif int(i) == 7:
        stepper.terminate()
    else:
        print('Falsche Eingabe')
    
def main():
    stepper = Stepper(22, 23, 24, 25)
    
    while True:
        t = Thread(target=user_interaction, args=(stepper,))
        t.start()
        t.join()
    
    
def cleanup():
    GPIO.cleanup()
    

if __name__ == '__main__':
    setup()
    main()
    # cleanup()
