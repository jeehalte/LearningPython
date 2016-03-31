import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
led_gpio = 17
GPIO.setup(led_gpio, GPIO.OUT)

for i in range(1, 10):
	GPIO.output(led_gpio, not GPIO.input(led_gpio))
	if i % 2 == 0:
		sleep(1)
	else:
		sleep(0.5)
GPIO.cleanup()
