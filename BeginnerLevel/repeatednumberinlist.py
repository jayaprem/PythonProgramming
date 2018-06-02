n=int(input())
list1=[]
list2=[]
count=0
for i in range(0,n):
    r=int(input())
    if(type(r)==int):
        list1.append(r)
for j in range(0,n):
    c=list1.count(list1[j])
    if(c>1):
        if(list1[j] not in list2):
            list2.append(list1[j])
        else:
            count=count+1
if(count==n):
    print ("unique")
else:
    sorted(list2)
    for x in range(len(list2)):
        print(list2[x],end=' ')
        
    
          


