seed=12345

a=1664525
c=1013904223
m=2**32

def generate():
	global seed
	seed =(a * seed +c)%m
	return seed
	
for i in range(10):
	print(generate())
