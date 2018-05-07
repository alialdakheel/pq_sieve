#!/usr/bin/env python

from gmpy2 import gcdext
from timeit import default_timer as timer
import sys

# Global BEGIN

# Global END

''' 
* @param a, b coprime 
* @param a0, a1 result of n mod a and n mod b  
* @return perm_n the result of n mod a*b
'''
def calc_modn(a,b,a0,a1):
    gcd, s, d = gcdext(a,b)
    perm_n = s*a0*a + d*a1*b
    return perm_n


def main(n, num_primes):
    pfp = open('primes.txt','r') #prime file pointer // a list of primes
    wfp = open("mod_nonp.json", "w") # write file pointer (json output)
    # prepare prime list
    primes = pfp.read().split()
    del primes[0:3] # delete first three primes namely [2,3,5]

    # init loop
    calc_modn(primes[0],primes[1])

    for i in 


if __name__ == '__main__':
    start_time = timer()
    main(sys.argv[1], sys.argv[2])
    diff_time = timer() - start_time
    print("Time: " + str(diff_time) )
