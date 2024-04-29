import os

dir_path= "/home/ccf"
extensions=[",jpg",".jpeg",".png",".gif",".bmp",".pdf"]

for filename in os.listdir(dir_path):
	if any(filename.endswith(ext)for ext in extensions):
		print(filename)
		

