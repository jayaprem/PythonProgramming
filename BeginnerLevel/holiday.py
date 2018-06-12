hol=['saturday','sunday']
norm=['monday','tuesday','wednesday','thursday','friday']
n=raw_input()
if n in hol:
	print "yes"
elif n in norm:
	print "no"
else:
	print "not valid"
