def logo():
	print("""
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                %
%                 # Coded By @trouble1_raunak                    %
%                                                                %
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         
""" )

import requests
import os
import sys
from requests.exceptions import HTTPError
from urllib3.exceptions import InsecureRequestWarning
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
print "(+) Result will be saved in folder name " + foldername + "/"
print ""
os.system("if [ -f potential.txt ]; then rm potential.txt potential_result.txt; fi")
isdir = os.path.isdir(foldername)
if isdir == True:
	os.system("rm -r " + foldername +"/")
	
os.system("mkdir " + foldername)
os.system('mkdir '+foldername+'/status/')
for line in f:
	try:
		m = m +1
		line = line.strip('\n')
		req = requests.get(url = line, allow_redirects=True, verify=False )
		res = req.text
		status = req.status_code
		if(len(res) > int(length)):
			os.system('echo '+ line + ' >> '+ foldername +'/potential.txt')
			result = str("Line No: " + str(m) + " " +line + " ----->  Len: "+ str(len(res)))
			os.system("echo '" + line + " -----> Len: " + str(len(res)) + "' >> " + foldername +"/potential_result.txt")
			print result
			
		req_status = requests.get(url = line, allow_redirects=False, verify=False )
		status =  str(req_status.status_code)
		result1 = str(line )
		file_name = foldername + "/status/"+status + ".txt"
		os.system("echo '" + result1 + "' >> " + file_name)

	#except requests.exceptions.ConnectionError as Ex:
	#	pass
	#except requests.exceptions.TooManyRedirects as e:
	#	pass
	except Exception as e:
		pass

