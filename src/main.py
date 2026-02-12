import adafruit_dht
import board
import time
import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dht = adafruit_dht.DHT22(board.D4)

while True:
	try:
		temp = dht.temperature
		hum = dht.humidity
		temp = (temp * (9/5) + 32) 
		print(temp)

		temp = struct.pack('!f', temp)
		sock.sendto(temp, ("192.168.86.29", 35423))
	except RuntimeError as e:
		print("error")
	time.sleep(2)
