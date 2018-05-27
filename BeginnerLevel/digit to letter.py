a=["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
b=["ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN","NINTEEN"]
c=["TEN","TWENTY","THIRTY","FOURTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINTY"]
file=open("d:\sample.txt","r+")
number=file.read()
no=int(number)
if(no<9999):
	if(no>=1000):
		t=no/1000
		no=no%1000
		print "".join((a[t-1],"thousand"))
	if(no>=100):
		t=no/100
		no=no%100
		print "".join((a[t-1],"hundred and"))
	if(no>10 and no<20):
		t=no%10
		print "".join(b[t-1])
	if(no==10):
		t=no/10
		print "".join(c[t-1])
	if(no>19 and no<100):
		t=no/10
		no=no%10
		print "".join(c[t-1])
	if(no<10 and no!=0):
		print "".join(a[no-1])
else:
	print "enter  a small number"
