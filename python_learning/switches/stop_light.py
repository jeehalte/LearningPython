import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

red_led_gpio = 23 # pin number of red LED
yellow_led_gpio = 12 # pin number of yellow LED
green_led_gpio = 21 # pin number of green LED
switch_gpio = 17 # pin number of switch 

GPIO.setup(red_led_gpio, GPIO.OUT) #edfine pin 22 as output
GPIO.setup(yellow_led_gpio, GPIO.OUT) #edfine pin 4 as output
GPIO.setup(green_led_gpio, GPIO.OUT) #edfine pin 4 as output
GPIO.setup(switch_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP) #define pin 17 as input with pull up pull down switch 
GPIO.output(red_led_gpio, True) # light up the red LED first
GPIO.output(yellow_led_gpio, False)
GPIO.output(green_led_gpio, False)

def start_stop_light():
	while(True):	
		if GPIO.input(red_led_gpio):
			sleep(2.0)
			GPIO.output(red_led_gpio, False)
			GPIO.output(yellow_led_gpio, False)
			GPIO.output(green_led_gpio, True)
		elif GPIO.input(yellow_led_gpio):
			sleep(1.0)
			GPIO.output(red_led_gpio, True)
			GPIO.output(yellow_led_gpio, False)
			GPIO.output(green_led_gpio, False)			
		elif GPIO.input(green_led_gpio):
			sleep(4.0)
			GPIO.output(red_led_gpio, False)
			GPIO.output(yellow_led_gpio, True)
			GPIO.output(green_led_gpio, False)			

try:
	start_stop_light()
except KeyboardInterrupt:
    GPIO.cleanup()
