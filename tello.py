#!/usr/bin/env python3

import socket

tello_address = ('192.168.10.1', 8889)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("", 9000))

message = "takeoff"

def send(message):
	try:
		sock.sendto(message.encode(), tello_address)	
	except Exception as e:
		print("Error")

def receive():
	try:
		resp, ip_address = sock.recvfrom(128)
		print("Received Message: {}".format(resp.decode(encoding="utf-8")))
	except Exception as e:
		print("error on receive")

send("battery?")

receive()

