def checkpass(password):
	"\ncheck complexity of the given password\n"
	rating=0
	length=len(password)
	
	if length>=8:
		rating+=1
		if length>=12:
			rating+=1
			
	if any(c.islower() for c in password):
		rating+=1
		
	if any(c.isupper() for c in password):
		rating+=1
		
	if any(c.isdigit() for c in password):
		rating+=1
		
	if any(c in "!@#$%^&*()_=,<>.?/[]{}\|~`;'"for c in password):
		rating+=1
		
	return rating
	
password=input("Enter the password : ")

rating = checkpass(password)
print(f"The password complexity rating is {rating}/6")

