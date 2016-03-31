import RPi.GPIO as GPIO # import the GPIO (genearl input/output library)
from time import sleep # import the sleep function

GPIO.setmode(GPIO.BCM) #set the GPIO board pin numbering i.e. pin number on board is the pin number being worked with

led_gpios = [17, 22] # array of pin numbers used

for i, gpio in enumerate(led_gpios): #looping through all pins being used and setting each other pin's state to low
    state = i % 2 == 0
    GPIO.setup(gpio, GPIO.OUT, initial=state) 

sleep(2.0)

for _ in range(20): # loop through 20 times
    states = [not GPIO.input(gpio) for gpio in led_gpios]
    GPIO.output(led_gpios, states) 
    sleep(0.5) # sleep 0.5 second

GPIO.cleanup()