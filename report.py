import microdotphat as dot
import Adafruit_DHT
import time


sensor = Adafruit_DHT.DHT11
pin = 23

dot.clear()
dot.set_rotate180(False)
dot.write_string('Hello_', kerning=False)
dot.show()
time.sleep(3)
dot.write_string(' P1X ', kerning=False)
dot.show()
time.sleep(1)


while True:
	dot.write_string('>LOAD<', kerning=False)
	dot.show()
	hum, temp = Adafruit_DHT.read_retry(sensor, pin)
	repeat=8
	while repeat>0:
		if hum is not None and temp is not None:
			dot.write_string('C {0:0.1f}'.format(temp), kerning=False)
			dot.show()
			time.sleep(2)

			dot.write_string('% {0:0.1f}'.format(hum), kerning=False)
			dot.show()
			time.sleep(2)
		else:
			dot.write_string('Error', kerning=False)
			dot.show()
			time.sleep(30)
			repeat = 0
		repeat -= 1
