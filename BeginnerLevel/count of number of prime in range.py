n=int(input())
m=int(input())
temp=0
for i in range(n,m+1):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count=1
    if(count==0):
        temp=temp+1
if(count!=0):
    print(temp)
