import os
#os.system('sudo ifconfig ens39 192.168.0.103')
#os.system('sudo ifconfig ens39 down')

os.system('sudo ifconfig ens39 192.168.0.111')
os.system('sudo ifconfig ens39 up')


from netaddr import *

ip=IPAddress('192.168.0.111')

print ip
