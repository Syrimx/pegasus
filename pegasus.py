import requests
import sys
import traceback
import os
import re
from random import randint
'''
Pegasus
---------
Web Scraping Wordlist Creator
usage:
python3 <script> <url> <wordlist name>
@Ely Schybol <-> 15.03.2022
'''
green = '\033[96m'
blurp = '\033[93m'
reset = '\033[0m'

def welcome():
	print(blurp+"\nWillkommen zu Pegasus ^_^ Hiermit können spezifische Wordlists erstellt werden"+reset)
	print(green+"================================================================================"+reset)
	print(green+"[+]Web Scraping..."+reset)

def fin(path):
	print(green+"================================================================================"+reset)
	print(green+"[+]Aufgabe erledigt ^_^"+reset)
	print(blurp+f"[+]Wordliste ist unter {path} zu finden"+reset)
	print(green+"================================================================================"+reset)

def main(url, wordlistName):
	welcome()
	path = os.path.join("/home/shibes/Dokumente/ethical/wordlist/own", f"{wordlistName}.txt") #change the path
	data = requests.get(url).text.split()
	with open(path, 'w') as dump:
		for i in data:
			if(re.findall("[<,>,=,\",:,;, \d,-]", i) == []):
				dump.write(f"{i}\n")
			else:
				continue
	fin(path)

if __name__ == '__main__':
	try:
		main(sys.argv[1], sys.argv[2])
	except:
		traceback.print_exc()
