#!/usr/bin/env python

for i in range(1,64,2):
	for j in range(1,64,2):
		result1 = (i * j + 1) % 64
		result2 = (i + j) % 64
		length1 = len(str(i)) + len(str(j)) + len(str(result1))
		length2 = len(str(i)) + len(str(j)) + len(str(result2))

		for x in range(0,6-length1):
			print "",

		print str(i) + " x " + str(j) + " + 1 = " + str(result1) + " mod 64",

		for x in range(0,6-length2):
			print "",

		print "     " + str(i) + " + " + str(j) + " = " + str(result2) + " mod 64"

