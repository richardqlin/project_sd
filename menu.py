
import Directory_change
#import IP_Addr_change
#import FireWall

print 'Please make your choice'

print 'Directory ---- 1'

print 'Ip address ---- 2'

print 'FireWall ---- 3'

choice=raw_input()

if choice =='1':
	Directory_change.function()

if choice =='2':
	IP_Addr_change.function()

if choice =='3':
	FireWall.function()

