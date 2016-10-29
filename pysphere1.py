from pysphere import VIServer

server=VIServer()

server.connect('127.0.0.1:443','THESTDOMAIN\','hohoho')



server.server.get_vm_by_name("[Shared] Windows Server 2008 R2 x64")

machine.power_on()

