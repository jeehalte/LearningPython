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

# Define the function to be called when the switch button is pressed. 
# This is denoted by the falling edge, as the pin will be going from high when 
# the switch is open and to low when the switch connects the pin to the ground.

def toggle_led(_):
	if GPIO.input(red_led_gpio):		
		GPIO.output(red_led_gpio, False)
		GPIO.output(yellow_led_gpio, False)
		GPIO.output(green_led_gpio, True)
	elif GPIO.input(yellow_led_gpio):
		GPIO.output(red_led_gpio, True)
		GPIO.output(yellow_led_gpio, False)
		GPIO.output(green_led_gpio, False)
	elif GPIO.input(green_led_gpio):
		GPIO.output(red_led_gpio, False)
		GPIO.output(yellow_led_gpio, True)
		GPIO.output(green_led_gpio, False)

# adding callback function to the swtich to fire the toggle_led function
# when the switch is toggled

# Here, the bouncetime parameter is used to limit the minimum time between the interrupts 
# being fired by the button changing state. This is a technique known as debounceing.

GPIO.add_event_detect(switch_gpio, GPIO.FALLING, callback=toggle_led, bouncetime=500)

try:
    while(True):    	
        sleep(5.0)
except KeyboardInterrupt:
    GPIO.cleanup()
