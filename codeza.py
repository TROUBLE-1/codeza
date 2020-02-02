def logo():

	print ('\033[94m' + """
                                          
          /|                                 
         / |                  
   _____|  |_____                                                         
  /_____   _____/                                                         
        |  | _      ____   ____   ____   _____  _____      _            
        |  || |    |####| |####| |####  |##### |#####     /#\           
        |  || |   |#      #    # |#   # |#|___    /#     /# #\          
        |  || |   |#      #    # |#   # |####    /#     /#/_\#\         
        |  ||/    |#____  #____# |#___# |#|__   /#___  /#/   \#\        
        | /        |####| |####| |####  |##### /##### /#/     \#\       
        |/                                                              
                    # Coded By Raunak Parmar - @trouble1_raunak         
                                                                          
	""" + '\033[00m')

import requests
import os
import sys
from requests.exceptions import HTTPError
from urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, Back, Style
import re
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if len(sys.argv) != 4:
	print "(+) usage: %s <file> <Min_Length> <Folder_name_to_create>" % sys.argv[0]
	print "(+) eg: %s alive.txt 500 ford" % sys.argv[0]
	print "(+) Note: List should contain http://"
	sys.exit(-1)

file = sys.argv[1]
length = sys.argv[2]
foldername = sys.argv[3]
logo()
m  = 0
f = open(file)
print ('\033[96m' + "(+) Result will be saved in folder name " + foldername + "/" + '\033[00m')
print ""
os.system("if [ -f potential.txt ]; then rm potential.txt potential_result.txt; fi")
isdir = os.path.isdir(foldername)
if isdir == True:
	os.system("rm -r " + foldername +"/")
	
os.system("mkdir " + foldername)
os.system('mkdir '+ foldername+'/status/')
os.system("mkdir " + foldername + "/error/")
for line in f:
	try:
		m = m +1
		line = line.strip('\r\n')
		req = requests.get(url = line, allow_redirects=True, verify=False )
		res = req.text
		forms = ["</form>", "password", "username", "methods="]
		forms_found = False
		for item in forms:    
			if item in res:
				forms_found = True
				found = item	
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
		if(len(res) > int(length)):
			try:
				os.system('echo '+ line + ' >> '+ foldername +'/potential.txt')
				r1 = re.findall("<title>(.+?)</title>",res)
				for x in range(len(r1)):
					title = " No Title"
					if r1[x] != None:  
						title = r1[x]
				# result in with_titles.txt
				
				os.system("echo '" + line + " -->  " + title + "' >> " + foldername + "/with_titles.txt")
				
					
				result = " " + ('\033[92m' +line + '\033[00m')+ ('\033[93m' +" --> " + '\033[00m') + ('\x1b[6;29;43m ' + 'Len:' + '\x1b[0m') + " " + ('\033[92m' + str(len(res)) + '\033[00m') + ('\033[94m' +" --> " + '\033[00m') +('\x1b[6;29;44m ' + 'Title:' + '\x1b[0m') +" " + ('\033[92m' + title + '\033[00m')
				
				CSI = "\x1B["
				full_result = (CSI+"29;45m" + "[ Line No: " + str(m) + " ]"+ CSI + "0m")+ result
				result1 = line + " --> " + "Len: " +str(len(res)) + " --> " + " Title: " + title
				os.system("echo '" + result1 + "' >> " + foldername +"/potential_result.txt")
				print full_result
			except UnicodeEncodeError as error:
					print ('\x1b[6;29;41m' + "  [Error: Line no "+ str(m) + ", " + "Url: " + line + "]"+ '\x1b[0m')+ ('\033[91m' + " There was error while updating result in with_title.txt" + '\033[00m')
					update = line + "[Error: Line no "+ str(m) + " ]"
					os.system("echo " + update + " >> " + foldername + "/error/title_error.txt")
					pass
		
		# urls with status code are been saved from here in status/ folder
		req_status = requests.get(url = line, allow_redirects=False, verify=False )
		status =  str(req_status.status_code)
		result2 = str(line )
		file_name = foldername + "/status/"+status + ".txt"
		os.system("echo '" + result2 + "' >> " + file_name)

	except requests.exceptions.ConnectionError as Ex:
		pass
	except requests.exceptions.TooManyRedirects as e:
		pass
	#except IndexError as error:
	#			pass	
	#except Exception as e:
	#	pass

