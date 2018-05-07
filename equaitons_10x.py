#!/usr/bin/env python

'''
for j in range(0,10,10):
	for i in [1,3,7,9]:
		#print  "10x+" + str(i+j)
		for x in range(0,10,10):
			for y in [1,3,7,9]:
				print str(i+j) + "	" + str(x+y) + "	" + str((i+j)*(x+y)) + "	" + str(i+j+x+y) + "	" + str(((i+j)*(x+y)) % 10) + "	" + str((i+j+x+y) % 10) + "	" + str(((i+j)*(x+y))/10) + "	" + str((i+j+x+y) / 10)
'''
#for j in range(0,7,7):
#	for i in range(0,7):
#		#print  "10x+" + str(i+j)
#		for x in range(0,7,7):
#			for y in range(0,7):
#				print("49x(x+j+" + str((i+j+x+y) / 7) + ") + " + "7(" + str((i+j+x+y) % 7) + "x+" + str(i) + "j+" + str(((i+j)*(x+y))/7) + ") + " + str((((i+j)*(x+y)) + 1) % 7) + '   '),
#				print("7(2x+j+" + str((i+j+x+y) / 7) + ") + " + str((i+j+x+y) % 7))
#
#for j in range(0,11,11):
#	for i in range(0,11):
#		#print  "10x+" + str(i+j)
#		for x in range(0,11,11):
#			for y in range(0,11):
#				print("11^2x(x+j+" + str((i+j+x+y) / 11) + ") + " + "11(" + str((i+j+x+y) % 11) + "x+" + str(i) + "j+" + str(((i+j)*(x+y))/11) + ") + " + str((((i+j)*(x+y)) + 1) % 11) + '   '),
#				print("11(2x+j+" + str((i+j+x+y) / 11) + ") + " + str((i+j+x+y) % 11))
#

from pprint import pprint
import json
mod_7 = {}
mod_11 = {}

fp = open("mod_p.json", "w")

for i in range(0,7):
    for j in range(0,7):
        if ((i+j) % 7) in mod_7.get((i*j+1) % 7,[-1,-1]):
            continue
        mod_7.setdefault((i*j+1) % 7,[]).append((i+j) % 7)

for i in range(0,11):
    for j in range(0,11):
        if ((i+j) % 11) in mod_11.get((i*j+1) % 11,[-1,-1]):
            continue
        mod_11.setdefault((i*j+1) % 11,[]).append((i+j) % 11)

mod_p = {7:mod_7, 11:mod_11}
json.dump(mod_p,fp)

#pprint(mod_p)
