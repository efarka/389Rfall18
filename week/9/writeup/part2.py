#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
ctr=0
while True:
	data = s.recv(1024)
	print(data)

	lines=data.split('\n')
	words=lines[1].split(' ')
	if ctr==0:
		words=lines[3].split(' ')
	command='result=hashlib.' + words[3] + '("'+words[6] + '").hexdigest()'
	exec(command)
	s.sendall(result + '\n')
	ctr = ctr+1
#print(words[3] + words[6])
# close the connection
s.close()

