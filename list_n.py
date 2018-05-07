#!/usr/bin/env python

fp = open("primes.txt","r")

l = fp.read().split()

#print type(l)
#print l[5:10]

for i in l:
	for j in l[l.index(i):] :
		prod = int(j) * int(i)
		if (len(str(prod)) > 3): 
			if (((prod + 1) % 3 == 0) & (int(str(prod)[-3]) % 2 != 0)):
				print prod 	
