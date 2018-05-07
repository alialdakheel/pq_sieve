#!/usr/bin/env python

from timeit import default_timer as timer
import json
import sys

def main(av):
    num_p = int(av[1]) #number of primes to be used.

    pfp = open('primes.txt','r') #prime file pointer // a list of primes
    wfp = open("mod_nonp.json", "w") # write file pointer (json output)

    # prepare prime list

    primes = pfp.read().split()
    del primes[0:3] # delete first three primes namely [2,3,5]

    mod_nonp = dict()
    sm_num = 1
    for p in primes[0:num_p]:
        sm_num *= int(p)

    #mod_p[p]= dict()
    for i in range(1,sm_num):
        for j in range(1,sm_num):
            if (i*j) % 7 == 0 or (i*j) % 11 == 0:
                continue
            if ((i+j) % sm_num) in mod_nonp.get((i*j+1) % sm_num,[-1,-1]):
                continue
            #mod_p[p].setdefault((i*j+1) % p,[]).append((i+j) % p)
            mod_nonp.setdefault((i*j+1) % sm_num,[]).append((i+j) % sm_num)

    # Sorting block
    type(mod_nonp)
    for k,i in mod_nonp.items():
        mod_nonp[k] = sorted(i)


    json.dump(mod_nonp,wfp)
    return

if __name__ == "__main__":
    start = timer()
    main(sys.argv)
    diff = timer() - start
    print("time: " + str(diff))
