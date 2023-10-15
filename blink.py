from gpiozero import LED
import time

led = LED(4)

while True:
	led.on()
	print("LED ON")
	time.sleep(1)
	led.off()
	print("LED OFF")
	time.sleep(1)	
