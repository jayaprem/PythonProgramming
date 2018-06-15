a=int(input())
b=int(input())
list1=[]
for i in range(1,100000):
	if(i%a==0 and i%b==0):
		list1.append(i)
sorted(list1)
print list1[0]
