#domain to ip converter
import socket #for connection to device
import pyfiglet #for create banner
from termcolor import colored #for colorfull banner

print(colored("************* Domain To IP Converter *************","red"))
print(colored("************* Create By Anayet Ullah *************","green"))

banner=colored(pyfiglet.figlet_format("Domain To IP"),"green") # Banner
print(banner)

domain_name=input("Enter Your Target Domain:")
ip= socket.gethostbyname(domain_name)
print("Ip for {} : {}".format(domain_name,ip))