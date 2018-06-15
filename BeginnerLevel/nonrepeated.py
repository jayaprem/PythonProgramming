n=int(input())
list1=[]
for i in range(0,n):
	p=int(input())
	list1.append(p)
for j in range(0,n):
	c=list1.count(list1[j])
	if(c==1):
		print list1[j]
