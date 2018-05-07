#!/usr/bin/env python

from gmpy2 import invert
from json import load
import json
from subprocess import call
from itertools import product
from pprint import pprint
from timeit import default_timer as timer

# Global
num_primes = 4 # warning: supports only 2 primes ATM

# for the time being support only 2 primes
call(["./mod_p_gen.py", str(num_primes)])

# import and open the json file of n mod p to, r mod p mapping.
fp = open('mod_p.json','r')
modp = load(fp)
primelist = modp.keys()

#num_primes = len(modp)


# End Gloabal

def gen_permlist(n0 ,n1):

    # print(modp)
    # prep mod prime all combinations tuples primelist = []
    comblist = []
    primelist = []
    for n in [n0,n1]:
        comblist.append(modp[n].keys())
        # primelist.append(int(p))

    combtuples = []
    keys = []
    for i in product(*comblist):
        keys.append(eval_eq(int(i[0]),int(i[1]),int(n0),int(n1)))
        combtuples.append((str(i[0]) + ' , ' + str(i[1])))


    #pprint(combtuples)
    # calculate new r mod prodp  for two primes (for the time being)
    combdict = {}
    for i in range(0,len(combtuples)):
        for a0 in modp.get(str(n0)).get(combtuples[i].split()[0]):
            for a1 in modp.get(str(n1)).get(combtuples[i].split()[2]):
            #for a1 in modp[str(n1)][tupl[1]]:
                combdict.setdefault(str(keys[i]) ,[]).append(eval_eq(int(a0),int(a1),int(n0),int(n1)))

    # Sorting block
    for k,i in combdict.items():
        combdict[k] = sorted(i)

    # print(combdict)
    wfp = open("mod_prodp.json", "w") # write file pointer (json output)
    json.dump(combdict,wfp)
    return combdict

def eval_eq(a0, a1, n0, n1):
    return (((int(invert(n1, n0)) % n0) * (a0 - a1) ) % n0 ) * n1 + a1

def main():
    n0 = primelist[0]
    n1 = primelist[1]
    print (n0 + '   ' +  n1)
    ret_dict = gen_permlist(n0,n1)
    del modp[n0]
    del modp[n1]
    modp[str(int(n0) * int(n1))] = ret_dict
    p_i = 1
    while (p_i < len(primelist) - 1):
        n0 = str(int(n0) * int(n1))
        n1 = str(primelist[int(p_i) + 1])
        print (n0 + '   ' +  n1)
        ret_dict = gen_permlist(n0,n1)
        # if ( p_i == len(primelist) - 1):
        # else:
        del modp[n0]
        del modp[n1]
        modp[str(int(n0) * int(n1))] = ret_dict
        # print(modp)
        p_i += 1
    return


if __name__ == '__main__':
    start = timer()
    main()
    diff = timer() - start
    print("time: " + str(diff))
