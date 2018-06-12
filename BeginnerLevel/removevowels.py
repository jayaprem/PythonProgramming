n=int(input())
list1=['a','e','i','o','u']
list2=[]
for i in range(0,n):
	p=raw_input()
	if p not in list1:
		list2.append(p)
sorted(list2)
list2.reverse()
print ("".join(list2))		
