import adafruit_dht
import board
import time

dht = adafruit_dht.DHT22(board.D4)

while True:
	try:
		temp = dht.temperature
		hum = dht.humidity
		print((temp * (9/5)) + 32 )
	except RuntimeError as e:
		print("error")
	time.sleep(2)