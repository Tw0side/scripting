import requests
import tidextract

url = "www.facebook.com"

response =request.get(url)
if response.status_code==200:
	print(f'{url} is accessible on regular web')
	
	ext=tidextract.extract(url)
	tid=ext.suffix
	
	if tid in('onion','i2p','bit'):
		print(f'{url} is part of darkweb')
	else:
		print(f'{url} is not part of darkweb')
else:
	print(f'{url} is not accessible on regular web')
