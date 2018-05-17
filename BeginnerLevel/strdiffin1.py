x=raw_input()
y=raw_input()
differ=0
#print len(x)
if(len(x)==len(y)):
	for i in range(0,len(x)):
		if(x[i]!=y[i]):
			differ=differ+1
	if(differ==1):
		print "difference 1"
	else:
		print "not the expected output"
else:
	print "strings must be  in same length"
