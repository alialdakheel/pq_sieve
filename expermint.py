#!/usr/bin/env python

'''
for j in range(0,10,10):
	for i in [1,3,7,9]:
		#print  "10x+" + str(i+j)
		for x in range(0,10,10):
			for y in [1,3,7,9]:
				print str(i+j) + "	" + str(x+y) + "	" + str((i+j)*(x+y)) + "	" + str(i+j+x+y) + "	" + str(((i+j)*(x+y)) % 10) + "	" + str((i+j+x+y) % 10) + "	" + str(((i+j)*(x+y))/10) + "	" + str((i+j+x+y) / 10)
'''
'''
for j in range(0,99,10):
	for i in [1,3,7,9]:
		#print  "10x+" + str(i+j)
		for x in range(0,99,10):
			for y in [1,3,7,9]:
				print "10000x(x+j+" + str((i+j+x+y) / 100) + ") + " + "100(" + str((i+j+x+y) % 100) + "x+" + str(i) + "j+" + str(((i+j)*(x+y))/100) + ") + " + str(((i+j)*(x+y)) % 100),
				print "	" + "100(2x+j+" + str((i+j+x+y) / 100) + ") + " + str((i+j+x+y) % 100)
				for s in range(1,100,1):
					
'''
'''
for j in range(0,10,10):
	for i in [1,3,7,9]:
		#print  "10x+" + str(i+j)
		for x in range(0,10,10):
			for y in [1,3,7,9]:
				print "100x(x+j+" + str((i+j+x+y) / 10) + ") + " + "10(" + str((i+j+x+y) % 10) + "x+" + str(i) + "j+" + str(((i+j)*(x+y))/10) + ") + " + str(((i+j)*(x+y)) % 10)
				for s in range(1,100,1):
					b = False
					if ((((i+j+x+y) % 10) * s) % 10 == 2):
						print "x coeff = 2 at " + str(s)
						b = True
					if ((i * s) % 10 == 1):
						print "j coeff = 1 at " + str(s)
						b = True 
					if (b): 
						b= False

'''

for i in range(3,99994,10):
	print str(i) + "	" + str(i**2)
