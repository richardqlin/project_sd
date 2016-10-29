import socket
import commands
import re
import os
name=socket.gethostname()
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com',0))

ipaddress=s.getsockname()[0]
s.close()


print name

ip=socket.gethostbyname(name)

print ip

print ipaddress

ipv4 = re.search(re.compile(r'(?<=ens )(.*)(?=\/)', re.M), os.popen('ip addr show eth0').read()).groups()[0]

