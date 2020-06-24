#!/usr/bin/env python3

import requests
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from requests.exceptions import HTTPError
from urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, Back, Style
import re
import time
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def logo():

	print ('\033[94m' + """
 ___________________________________________________________________
|                                                                   |
|          /|                                                       |
|         / |                             This Is my first tool :)  |
|   _____|  |_____                                                  |
|  /_____   _____/                                                  |
|        |  | _      ____   ____   ____   _____  _____      _       |
|        |  || |    |####| |####| |####  |##### |#####     /#\      |
|        |  || |   |#      #    # |#   # |#|__     /#     /# #\     |
|        |  || |   |#      #    # |#   # |####    /#     /#/_\#\    |
|        |  ||/    |#____  #____# |#___# |#|___  /#___  /#/   \#\   |
|        | /        |####| |####| |####  |##### /##### /#/     \#\  |
|        |/                                                         |
|                    # Coded By Raunak Parmar - @trouble1_raunak    |
|___________________________________________________________________|
	""" + '\033[00m')


if sys.version_info[0] < 2:
	print(('\033[91m' + "[!]" + '\033[00m')+" Python 3 required")
	exit()

def help():
	print("(+) usage: %s [file] [output]" % str(sys.argv[0]))
	print("(+) eg: %s domain.txt ford" % sys.argv[0])
	print()
	print("Give file name only for no output")
	print("(+) eg: codeza.py domain.txt")
	sys.exit(-1)
	
try:
	if (sys.argv[1]) == '-h':
		help()
except Exception as e:
	help()

# Arguments

file = sys.argv[1]

try:
	foldername = sys.argv[2]
except Exception as e:
	pass

logo()

try:
	f = open(file)
except Exception as e:
	print((str('\x1b[6;29;41m[' + file + " not exist!]" + '\x1b[0m')))
	sys.exit(0)

def contactMe():
	print()
	try:
		print(('\033[96m' + "(+) Result will be saved in folder name " + foldername + "/ " + '\033[00m'))
	except Exception as e:
		print(('\033[96m' + "(+) Result is not beening saved" + '\033[00m'))
		pass
	print(('\033[96m' + "(+) Contact me on twitter for any suggestion or help- @trouble1_raunak" + '\033[00m'))
	print ("")
	
def createFolders():
	try:
		os.system("mkdir " + foldername)
		os.system('mkdir '+ foldername+'/status/')
		os.system("mkdir " + foldername + "/error/")
	except Exception as e:
		pass

try:
	# Is there a directory?
	isdir = os.path.isdir(foldername)

	# Validating base folder
	if isdir == True:

		print((('\033[91m' + "[!] " + '\033[00m') + ('\x1b[6;29;41m' + foldername + "/"+ '\x1b[0m') + " folder already exits"))

		
		# everything in this IF statement logic depends on user input
		userInput1 = input(('\033[93m' + "[!] " + '\033[00m') + "Delete current folder? (y/n): ")
		if userInput1 == "y":
			os.system("rm -r ./" + foldername)
			createFolders()
			print((('\033[92m' + "[!] " + '\033[00m') + foldername +"/" + " Deleted, creating a new one"))
			contactMe()
			
		elif userInput1 == "n":
			foldername = input(('\033[92m' + "[!] " + '\033[00m') + "Type the name of the new folder: ")
			isdir = os.path.isdir(foldername)
			if isdir == True:
				print((('\033[91m' + "[!] " + '\033[00m') + "Please provide new folder name :|"))

				print((('\033[91m' + "[!] " + '\033[00m') +"Bye :)"))
				sys.exit()
			else:
				createFolders()
				contactMe()
		else:
			print(('\033[91m' + "[!] " + '\033[00m') + "Wrong input :(")
			sys.exit()
		
	else:
		contactMe()
		createFolders()
except Exception as e:
	contactMe()
	pass
	
print()




def main(line):
	try:
		# Request made here
		if "http://" in line or "https://" in line:
			line = line
		else:
			line = "http://" + line

	#	req = requests.get(url = line, allow_redirects=True, verify=False , timeout=10.00)
	#	if req.status_code ==  301:
	#		line = "https://" + line
		req = requests.get(url = line, allow_redirects=True, verify=False )
			
		res = req.text
		forms = ["</form>", "password", "username", "methods="]
		forms_found = False
		
		headers = req.headers
		
		if "Server" in headers:
			server = ('\033[96m' +" --> " + '\033[00m')+ ('\x1b[6;29;46m ' + 'Server:' + '\x1b[0m') +('\033[96m ' + headers['Server'] + '\033[00m')
			server1 = headers['Server']
		elif "X-Powered-By" in headers:
			server = ('\033[96m' +" --> " + '\033[00m') + ('\x1b[6;29;46m ' + 'Server:' + '\x1b[0m') +('\033[96m ' + headers['X-Powered-By'] + '\033[00m')
			server1 = headers['X-Powered-By']

		else:
			server = ""
			server1 = ""
		
		
		# check for forms
		for item in forms:    
			if item in res:
				forms_found = True
				found = item
		# for Dom XSS
		if forms_found:
			try:
				os.system("echo '" + line + " --> contains: " + found +"' >> " + foldername +"/contains_form.txt")
			except Exception as e:
				pass
			
		Dom_xss = ['document.URL', 'document.documentURI', 
					'location', 'location.href', 
					'location.search', 'location.hash', 
					'document.referrer', 'window.name', 
					'eval', 'setTimeout','setInterval', 
					'document.write', 'document.writeIn', 
					'innerHTML', 'outerHTML' ]
		
		Dom_xss_possible = False
		for item in Dom_xss:    
			if item in res:
				Dom_xss_possible = True
				found = item
		if Dom_xss_possible:
			try:
				os.system("echo '" + line + " --> contains: "+ found+ "' >> " + foldername + "/possible_Dom_XXS.txt" )
			except Exception as e:
				pass
		status = req.status_code

		try:
			os.system('echo '+ line + ' >> '+ foldername +'/potential.txt')
		except Exception as e:
			pass
		
		
		r1 = re.findall("<title>(.+?)</title>",res)
		if not r1:  
			title = ('\033[91m' + " No Title" + '\033[00m')
			title1 = "" 

		else:
			title = r1[0]
			
			title1 = ('\033[94m' +" --> " + '\033[00m') +('\x1b[6;29;44m ' + 'Title:' + '\x1b[0m') +" " + ('\033[92m' + title + '\033[00m')
			cmd = str(line + " --> " + title )
			try:
				os.system("echo '" + cmd + "' >> " + foldername + "/with_titles.txt")
			except Exception as e:
				pass
		# result in with_titles.txt
		
		if (len(res)) != 0:
			res = ('\033[93m' +" --> " + '\033[00m') + ('\x1b[6;29;43m ' + 'Len:' + '\x1b[0m') + " " + ('\033[92m' + str(len(res)) + '\033[00m')
		else:
			res = ""
		
		result = " " + ('\033[92m' +line + '\033[00m')+ res + title1 + server

		CSI = "\x1B["
		# full result
		full_result = (CSI+"29;45m" + "[ " + str(status) + " ]"+ CSI + "0m")+ result
		
		result1 = line + " --> " + "Len: " +str(len(res)) + " --> " + " Title: " + title1 + " Server: " + server1

		# upadating result
		try:
			os.system("echo '" + str(full_result) + "' >> " + foldername +"/color.txt")
			os.system("echo '" + str(result1) + "' >> " + foldername +"/potential_result.txt")
		except Exception as e:
			pass
		print (full_result)
					
			
		
		# urls with status code are been saved from here in status/ folder
		req_status = requests.get(url = line, allow_redirects=False, verify=False )
		status =  str(req_status.status_code)
		result2 = str(line )
		
		try:
			file_name = foldername + "/status/"+status + ".txt"
			os.system("echo '" + result2 + "' >> " + file_name)
		except Exception as e:
			pass
	
	
	# List of Possible Exceptions begins from here
	  	
	
	except Exception as e:
		errname = type(e).__name__
		print((str('\x1b[6;29;41m' + "[Error Url: " + str(line) + "]"+ '\x1b[0m')+ ('\033[91m ' + str(errname) + '\033[00m')))
		print ("")
		try:	
			os.system("echo " + line + " >> " + foldername + "/error/"+ str(errname) +".txt")
		except Exception as e:
			pass	
		pass


processes = []
with ThreadPoolExecutor(max_workers=20) as executor:
	for line in f:
		line = line.strip('\r\n')
		processes.append(executor.submit(main, line))

for task in as_completed(processes):
	(task.result())

print()
print(('\033[92m' + "(+) " + '\033[00m')+ " Done :)")
