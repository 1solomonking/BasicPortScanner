#!/usr/bin/python

import socket
from  termcolor import colored

socket.setdefaulttimeout(1)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("[*] Enter The Host To Scan: ")

def portscanner(port):
	if sock.connect_ex((host,port)):
		print (colored("[!!] Port %d is closed" % (port), 'red'))
	else:
		print (colored("[*] Port %d is Open" % (port), 'greeen'))

for port in range(1,1000):
	portscanner(port)
