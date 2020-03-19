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

if sys.version_info[0] > 2:
	print(('\033[91m' + "[!]" + '\033[00m')+" Python 2 required")
	exit()


if len(sys.argv) != 3:
	print ("(+) usage: %s <file> <Min_Length> <Folder_name_to_create>" % str(sys.argv[0])) 
	print ("(+) eg: %s alive.txt 500 ford" % sys.argv[0])
	print ("(+) Note: List should contain http:// or https://")
	sys.exit(-1)

# Arguments
file = sys.argv[1]
foldername = sys.argv[2]
logo()
m  = 0
f = open(file)

def contactMe():
	print("")
	print ('\033[96m' + "(+) Result will be saved in folder name " + foldername + "/ " + '\033[00m')
	print ('\033[96m' + "(+) Contact me on twitter for any suggestion or help- @trouble1_raunak" + '\033[00m')
	print ("")
	
def createFolders():
	os.system("mkdir " + foldername)
	os.system('mkdir '+ foldername+'/status/')
	os.system("mkdir " + foldername + "/error/")

# Is there a directory?
isdir = os.path.isdir(foldername)

# Validating base folder
if isdir == True:
	time.sleep(0.3)
	print(('\033[91m' + "[!] " + '\033[00m') + ('\x1b[6;29;41m' + foldername + "/"+ '\x1b[0m') + " folder already exits")
	time.sleep(0.3)
	
	# everything in this IF statement logic depends on user input
	userInput1 = raw_input(('\033[93m' + "[!] " + '\033[00m') + "Delete current folder? (y/n): ")
	if userInput1 == "y":
		os.system("rm -r ./" + foldername)
		createFolders()
		print (('\033[92m' + "[!] " + '\033[00m') + foldername +"/" + " Deleted, creating a new one")
		contactMe()
		
	elif userInput1 == "n":
		foldername = raw_input(('\033[92m' + "[!] " + '\033[00m') + "Type the name of the new folder: ")
		isdir = os.path.isdir(foldername)
		if isdir == True:
			print(('\033[91m' + "[!] " + '\033[00m') + "Please provide new folder name :|")
			time.sleep(0.4)
			print (('\033[91m' + "[!] " + '\033[00m') +"Bye :)")
			sys.exit()
		else:
			createFolders()
			contactMe()
	else:
		print ('\033[91m' + "[!] " + '\033[00m') + "Wrong input :("
		sys.exit()
	
else:
	contactMe()
	createFolders()
	
print




def main(line):
	try:
		t = time.localtime()
		m = time.strftime("%H:%M:%S", t)
		
		# Request made here
		req = requests.get(url = line, allow_redirects=True, verify=False )
		res = req.text
		forms = ["</form>", "password", "username", "methods="]
		forms_found = False

		#Search for server info
		headers = req.headers
		if "Server" in headers:
			server = ('\033[96m' +" --> " + '\033[00m')+ ('\x1b[6;29;46m ' + 'Server:' + '\x1b[0m') +('\033[96m ' + headers['Server'] + '\033[00m')
			server1 = headers['Server']
		elif "X-Powered-By" in headers:
			server = ('\033[96m' +" --> " + '\033[00m') + ('\x1b[6;29;46m ' + 'Server:' + '\x1b[0m') +('\033[96m ' + header['X-Powered-By'] + '\033[00m')
			server1 = header['X-Powered-By']
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
			os.system("echo '" + line + " --> contains: " + found +"' >> " + foldername +"/contains_form.txt")
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
			os.system("echo '" + line + " --> contains: "+ found+ "' >> " + foldername + "/possible_Dom_XXS.txt" )
		status = req.status_code

		os.system('echo '+ line + ' >> '+ foldername +'/potential.txt')
		r1 = re.findall("<title>(.+?)</title>",res)

		if not r1:  
			title = ('\033[91m' + " No Title" + '\033[00m')
			title1 = " No Title" 

		else:
			title = r1[0]
			title = title.replace(u'\u200e', '')
			title = title.replace(u'\xa0', '')
			title1 = title
			cmd = str(line + " --> " + title )
			os.system("echo '" + cmd + "' >> " + foldername + "/with_titles.txt")
		# result in with_titles.txt
	
		
		result = " " + ('\033[92m' +line + '\033[00m')+ ('\033[93m' +" --> " + '\033[00m') + ('\x1b[6;29;43m ' + 'Len:' + '\x1b[0m') + " " + ('\033[92m' + str(len(res)) + '\033[00m') + ('\033[94m' +" --> " + '\033[00m') +('\x1b[6;29;44m ' + 'Title:' + '\x1b[0m') +" " + ('\033[92m' + title + ' \033[00m') + server

		CSI = "\x1B["
		# full result
		full_result = (CSI+"29;45m" + "[ " + str(m) + " ]"+ CSI + "0m")+ result
		result1 = line + " --> " + "Len: " +str(len(res)) + " --> " + " Title: " + title1 + " Server: " + server1

		# upadating result
		os.system("echo '" + str(result1) + "' >> " + foldername +"/potential_result.txt")
		print (full_result)
					
			
		
		# urls with status code are been saved from here in status/ folder
		req_status = requests.get(url = line, allow_redirects=False, verify=False )
		status =  str(req_status.status_code)
		result2 = str(line )
		file_name = foldername + "/status/"+status + ".txt"
		os.system("echo '" + result2 + "' >> " + file_name)
	
	
	# List of Possible Exceptions begins from here
	  
	
	except Exception as e:
		errname = type(e).__name__
		print (str('\x1b[6;29;41m' + "[Error Url: " + str(line) + "]"+ '\x1b[0m')+ ('\033[91m ' + str(errname) + '\033[00m'))
		print ("")
		os.system("echo " + line + " >> " + foldername + "/error/"+ str(errname) +".txt")
		pass

processes = []
with ThreadPoolExecutor(max_workers=20) as executor:
	for line in f:	
		line = line.strip('\r\n')
		processes.append(executor.submit(main, line))
		
for task in as_completed(processes):
	(task.result())
	
print ("")
print (('\033[92m' + "(+) " + '\033[00m')+ " Done :)")
