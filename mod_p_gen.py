#!/usr/bin/env python

import json
import sys

def main(av):
	num_p = int(av[1]) #number of primes to be used.

	pfp = open('primes.txt','r') #prime file pointer // a list of primes
	wfp = open("mod_p.json", "w") # write file pointer (json output)

	# prepare prime list

	primes = pfp.read().split()
	del primes[0:3] # delete first three primes namely [2,3,5]

	mod_p = dict()
	for p in primes[0:num_p]:
	    p = int(p)
	    mod_p[p]= dict()
	    for i in range(1,p):
	        for j in range(1,p):
	            if ((i+j) % p) in mod_p.get(p,{-1:-1}).get((i*j+1) % p,[-1,-1]):
	                continue
	            mod_p[p].setdefault((i*j+1) % p,[]).append((i+j) % p)

	json.dump(mod_p,wfp)

main(sys.argv)
