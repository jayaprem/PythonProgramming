n=int(input())
list1=[]
list2=[]
count=0
for i in range(0,n):
    r=int(input())
    if(r.isdigit()):
        list1.append(r)
for j in range(0,n):
    c=list1.count(list1[j])
    if(c>1):
        count=count+1
    else:
        list2.append(list1[j])
if(count==n):
    print ("repeated")
else:
    sorted(list2)
    for x in range(len(list2)):
        print(list2[x],end=' ')
        
        
    
          
