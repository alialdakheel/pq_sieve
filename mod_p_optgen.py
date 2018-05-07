#!/usr/bin/env python3

import json
import sys
from gmpy2 import invert

def main(av,n):
	# num_p = int(av[1]) #number of primes to be used.

	# pfp = open('primes.txt','r') #prime file pointer // a list of primes
	# wfp = open("mod_p.json", "w") # write file pointer (json output)

	# prepare prime list

        h = int(av)
        n = int(n)

        # inv_i_lst = []
        ni_1_lst = []
        r_lst = []
        for i in range(1,h):
            # if i in inv_i_lst :
            if i in ni_1_lst :
                continue
            inv_i = invert(i,h)
            # inv_i_lst.append(inv_i)
            ni_1 = n * inv_i % h
            # if ni_1 in r_lst:
                # continue
            ni_1_lst.append(ni_1)
            # a = h + (n % h) - i
            # ab = (i*a) % h
            # ab_2 = (ab**2) % h
            r = (i + ni_1 ) % h
            # if r in r_lst :
                # continue
            r_lst.append(r)
            if r != 0:
                r_h = h - r
                r_lst.append(r_h)
            print('i = ', i , 'inv_i = ', inv_i , ' ni_1 = ', ni_1, ' i*ni_1 = ', i * ni_1 % h, ' r = ', r ,  ' r^2 = ', r**2 % h)
            # print( 'r list :' )
            # print(r_lst)

	# json.dump(mod_p,wfp)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
