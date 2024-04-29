import os

def check()
	with open("log.txt","r")as f:
		data =f.read()
		
	if "key" in data:
		print("Keylogger detected")
		
	else:
		print("No keylogger")
		
check()
