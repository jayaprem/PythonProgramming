s=raw_input()
list1=[]
if(len(s)>=1 and len(s)<=100000):
	for i in range(0,len(s)):
		a=ord(s[i])+3
		list1.append( chr(a))
print "".join(list1)
GIVEN A STRING LENGTH OF N,PRINT THE ENCODED STRING BY ADDING 3 TO EACH CHARACTER
INPUT SIZE:1<=N<=100000
INPUT:RADAR
OUTPUT:UDGDU
