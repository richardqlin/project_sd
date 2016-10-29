import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

r=s.connect_ex(('198.168.0.111',9000))

if r==0:
	print 'port is open'

else:
	print 'port is not open'


