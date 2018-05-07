#!/usr/bin/env python

import json
import sys
from timeit import default_timer as timer
from pprint import pprint

def precompute(p):
	p = int(p) # prime to precompute

	wfp = open('mod_' + str(p) + '.json', 'w') # write file pointer (json output)

	# prepare prime list


	mod_p = dict()
        for i in range(1,p):
            for j in range(i,p):
                if ((i+j) % p) in mod_p.get(p,{-1:-1}).get((i*j+1) % p,[-1,-1]):
                    continue
                mod_p.setdefault((i*j+1) % p,[]).append((i+j) % p)

        # Sorting internal lists
        for i in mod_p.keys():
            mod_p[i]= sorted(mod_p[i])

        json.dump(mod_p,wfp)

        return

def main(av):
	num_p = int(av) #number of primes to be used.

	pfp = open('primes.txt','r') #prime file pointer // a list of primes
	primes = pfp.read().split()
	del primes[0:3] # delete first three primes namely [2,3,5]

        for p in primes[0:num_p]:
            start_time = timer()
            precompute(p)
            diff_time = timer() - start_time
            print ('Precompute ', p, 'time: ',diff_time)

        return 0

if __name__ == '__main__':
    main(sys.argv[1])
