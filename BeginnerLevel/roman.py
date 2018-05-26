p=raw_input()
ans=0
for i in p:
	if(i=='I'):
		sum=1
	elif(i=='IV'):
		sum=4
	elif(i=='V'):
		sum=5
	elif(i=='IX'):
		sum=9
	elif(i=='X'):
		sum=10
	ans=ans+sum
print ans	
