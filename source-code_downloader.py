
#!/usr/bin/python3

#Get any website source code just one click

import turtle #Animation input from user
import urllib.request as u #Source code read & download
import pyfiglet #banner package
from termcolor import colored

print(colored("******* Source Code Downloader *******","green"))
print(colored("******* Created By Anayet Ullah *******","blue"))
banner= colored(pyfiglet.figlet_format("Source Code Downloader"),"yellow") #Use for banner
print(banner)

domain_name=turtle.textinput("Domain Name ", "Url Address") #Animation input from user

source_code_open=u.urlopen(domain_name)
source_code_read=source_code_open.read()
print(source_code_read)