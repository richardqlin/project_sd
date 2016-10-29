import sys
import os

import time


#os.chdir('/remotely_deploy/')




def func():
	curDir=os.getcwd()
	print curDir
	print 'Create directory ---1 '
	print 'Rename directory ---2 '
	print 'Remove directory ---3'

	d=raw_input()

	if d=='1': 


		dir=raw_input('please enter your directory that will be created')

		try:
			os.stat(dir)
		except:
			os.mkdir(dir)
		os.chdir(curDir+'/'+dir)
		time.sleep(1)

		curDir=os.getcwd()
		print curDir

	elif d=='2':
		org_dir=raw_input('Please enter which directory replaced to: ')
		new_dir=raw_input('Please enter which directory replaced by: ')
		
		try:
			os.rename(org_dir,new_dir)
		except:
			
			os.path.exists(org_dir)
			
		time.sleep(1)

		curDir=os.getcwd()
		print curDir
	elif d=='3':
		dir=raw_input('please enter your directory will be removed: ')
		try:
			os.rmdir(dir)
		except:

			os.path.exists(dir)


		curDir=os.getcwd()
		print curDir

n=raw_input('enter y to directory change, else to quit: ')

while n=='y':
	func()
	n=raw_input('enter y to continue the directory change, else to quit:')
	


