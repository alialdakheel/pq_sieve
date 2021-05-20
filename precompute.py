#!/usr/bin/env python

import json
import sys
from sqlitedict import SqliteDict

def main(av):
    num_p = int(av[1]) #number of primes to be used.

    pfp = open('primes.txt','r') #prime file pointer // a list of primes

    # prepare prime list
    primes = pfp.read().split()
    del primes[0:3] # delete first three primes namely [2,3,5]

    mod_p = dict()
    for p in primes[0:num_p]:
        p = int(p)
        mod_p[p]= dict()
        for i in range(1,p):
            for j in range(1,p):
                if ((i+j) % p) in mod_p.get(p,{-1:-1}).get((i*j) % p,[-1,-1]):
                    continue
                mod_p[p].setdefault((i*j) % p,[]).append((i+j) % p)

    # print(mod_p)
    with SqliteDict("mod_p_store.sqlite") as store_dict:
        for k, v in mod_p.items():
            store_dict[k] = {key: sorted(val) for key, val in v.items()}
        store_dict.commit()

def precompute_c(c, p):
        mod_p = list()
        for i in range(1,p-1):
            for j in range(i+1 ,p-1):
                prod = (i*j) % p
                s = (i+j) % p
                if prod != c or s in mod_p:
                    continue
                mod_p.append((i+j) % p)
        return sorted(mod_p)

if __name__ == "__main__":
    main(sys.argv)
