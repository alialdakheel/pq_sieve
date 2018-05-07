#!/usr/bin/env python

'''
for j in range(0,10,10):
	for i in [1,3,7,9]:
		#print  "10x+" + str(i+j)
		for x in range(0,10,10):
			for y in [1,3,7,9]:
				print str(i+j) + "	" + str(x+y) + "	" + str((i+j)*(x+y)) + "	" + str(i+j+x+y) + "	" + str(((i+j)*(x+y)) % 10) + "	" + str((i+j+x+y) % 10) + "	" + str(((i+j)*(x+y))/10) + "	" + str((i+j+x+y) / 10)
'''

for j in range(0,100,10):
	for i in [1,3,7,9]:
		#print  "10x+" + str(i+j)
		for x in range(0,100,10):
			for y in [1,3,7,9]:
			#	print "10000x(x+j+" + str((i+j+x+y) / 100) + ") + " + "100(" + str((i+j+x+y) % 100) + "x+" + str(i) + "j+" + str(((i+j)*(x+y))/100) + ") + " + str(((i+j)*(x+y)) % 100)
				print "100(2x+j+" + str((i+j+x+y) / 100) + ") + " + str((i+j+x+y) % 100)

