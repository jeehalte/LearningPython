import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

switch_gpio = 17
GPIO.setup(switch_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while(True):
		state = not GPIO.input(switch_gpio)
		print "Switch is pressed: %d" % state
		sleep(1.0)
except KeyboardInterrupt:
	GPIO.cleanup()
