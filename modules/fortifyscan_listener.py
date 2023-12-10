import time
import os,sys
import socket
from pexpect import pxssh
import re
import argparse


purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

parser = argparse.ArgumentParser()
parser.add_argument('host', help='Target host SSH')
parser.add_argument('user', help='Target username SSH')
parser.add_argument('password', help='Target password SSH')
parser.add_argument('method', help=' SSH' )
args = parser.parse_args()
if args.host and args.user and args.password:
	host = args.host
	user = args.user	
	method = args.method
	password = args.password

def clear():
	os.system('clear')

def banner():
	os.system('python3 banner.py ')

def connect_ssh():
	print ('Start SSH mode')
	ssh = pxssh.pxssh()
	try:
		ssh.login(host, user , password)
		print (green+'Start session->'+host+default)
	except:
		print (red+'Error connect ssh'+default)
		sys.exit(1)
	while True:
		print ('Enter comand')
		try:
			cmd = raw_input(blue+'Cmd->'+default)
		except KeyboardInterrupt:
			print ("Detect Ctrl+C")
			sys.exit('Good bye ;)')
		if cmd == "exit":
			sys.exit('Good by ;)')

		ssh.sendline(cmd)
		ssh.prompt()
		data = ssh.before
		print (data)


def main():
	clear()
	banner()
	print ('Time: '+time.ctime())
	print (red+'Start FortifyListener'+default)
	print (green+'Target host -> '+yellow+host+default)
	print (green+'Target user -> '+yellow+user+default)
	print (green+'Target password-> '+yellow+password+default)
	if method == 'ssh':
		connect_ssh()
main()