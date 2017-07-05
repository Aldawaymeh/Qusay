#!/usr/bin/env python3

import urllib.request
from wordr import wordlist_read

read = wordlist_read()

def get_admin(url, loob):
	try:
		open_url = urllib.request.urlopen(url)
		for i in loob:
			i = i.rstrip("\n")
			curl = url+""+i
			try:
				open_url = urllib.request.urlopen(curl)
				print("-----------------------------------------")
				print(curl+":: found [+]")
				print("-----------------------------------------")
			except urllib.error.HTTPError as msg:
				print(curl+":: Not fond [-]")
				print(msg)
	except urllib.error.URLError as msg:
		print(url)
		print(msg)

print("""

   _____  .__       .___                                          .___
  /  _  \ |  |    __| _/____ __  _  _______  ___.__. _____   ____ |  |__
 /  /_\  \|  |   / __ |\__  \\ \/ \/ /\__  \<   |  |/     \_/ __ \|  |  \
/    |    \  |__/ /_/ | / __ \\     /  / __ \\___  |  Y Y  \  ___/|   Y  \
\____|__  /____/\____ |(____  /\/\_/  (____  / ____|__|_|  /\___  >___|  /
        \/           \/     \/             \/\/          \/     \/     \/

		int:~ x_man_aldawaymeh  facebook:~ m3roor
	date:~ 4/7/2017

""")



adminlist = input('[+] Enter Name list:~ ')
while adminlist == '':
	print("[~~Error buz adminlist None~~]")
	adminlist = input('[+] Enter Name list:~ ')
loob = read.list_read(adminlist)
url = str(input('[+] Enter url:~ '))
while url == '':
	print("[~~Error buz url None~~]")
	url = str(input('[+] Enter url:~ '))
get_admin(url, loob)
