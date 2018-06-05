n=int(input())
list=[]
count=0
list2=[]
for i in range(0,n):
    r=int(input())
    list.append(r)
for j in range(0,n):
     if(list[j]==j):
         list2.append(list[j])
     else:
        count=count+1        
if(count==n):
    print("-1")
else:
    sorted(list2)
    for i in range(len(list2)):
        print(list2[i])
