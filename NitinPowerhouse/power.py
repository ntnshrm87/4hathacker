#!/usr/bin/python

import os
import subprocess
from espeak import espeak

espeak.synth("This is Nitin's PowerHouse. You are welcome.")
espeak.synth("Enter 1: for normal shutdown...Enter 2: for normal reboot...Enter 3: for fast shutdown...Enter 4: for fast reboot...Enter 5: for suspending...")

a = 0

while a == 0:
	os.system("tput setaf 2")
	print '\n\n\t**************************************************************\n'
	os.system("tput sgr 0 1")
	print '\t\t\tWelcome to Nitin\'s PowerHouse\n'
	os.system("tput sgr 0 0")
	os.system("tput setaf 2")
	print '\t**************************************************************\n'
	os.system("tput setaf 7")
	print '\t\tEnter 1: for normal shutdown...\n'
	print '\t\tEnter 2: for normal reboot...\n'
	print '\t\tEnter 3: for fast shutdown...\n'
	print '\t\tEnter 4: for fast reboot...\n'
	print '\t\tEnter 5: for suspending...\n\n'
	

	os.system("tput setaf 3")
	a = int (raw_input ('\t\tEnter the option for power buttons: '))
	if a == 1:
		subprocess.check_call(['sudo', 'shutdown'])
		# os.popen("shutdown") and os.system not working
		break 
	elif a == 2:
		espeak.synth("The system is going to reboot normally...")
		#os.popen('reboot') is working here
		subprocess.check_call(['sudo', 'reboot'])
		break
	elif a == 3:
		espeak.synth("fast shutdown")
		os.system('init 0')
		break
	elif a == 4:
		espeak.synth("rebooting fastly...")
		os.system('init 6')
		break
	elif a == 5:
		subprocess.check_call(['sudo', 'pm-suspend'])		
		#os.popen("pm-suspend") is not working here
		break
	else: 
		espeak.synth("You opted for a wrong choice... Try Again")
		os.system("tput setaf 1")		
		print '\n\t\tEnter a correct choice'

os.system("tput setaf 7")
espeak.synth("Press enter to leave now...")
raw_input('\n\t\tPress Enter to leave now...')
