#!/usr/bin/env python

'''
Implementation of the Ahmed et.al. p+q search

psudocode:

	if n mod 10 == 1 then:
		if n mod 100 == 01 then:
			if n+1 mod 3 == 0 then:
				a1 = 300
				b1 = 102
				a2 = 300
				b2 = 198
				a3 = 60
				b3 = 30
				for k:
					check_eq(a1,b1)
					check_eq(a2,b2)
					check_eq(a3,b3)

		if n mod 100 == 21 then:
		if n mod 100 == 41 then:
		if n mod 100 == 61 then:
		if n mod 100 == 81 then:

		if n mod 100 == 11 then:
		if n mod 100 == 31 then:
		if n mod 100 == 51 then:
		if n mod 100 == 71 then:
		if n mod 100 == 91 then:

'''

import sys
import subprocess
import json
from math import ceil
from math import sqrt
from gmpy2 import mpz
from gmpy2 import is_square
from gmpy2 import isqrt
from timeit import default_timer

#Global

#num_primes = 2
#ret = subprocess.call(["./mod_p_gen.py", str(num_primes)])

pfp = open('mod_p.json','r')
mod_p = json.load(pfp)

#

def check_eq(r,n):
    #r = a * k + b
    interm = r**2 - 4*n
    #res = math.sqrt(interm)
    is_res = is_square(mpz(interm))
    #fplot.write(str(k) + "  " + str(r) + "  " + str(r % 7) + "  " + str(r % 11) + "  " + str(interm) + '    ' +  '\n')
    #print interm
    if (is_res):
        print("\n----------------------------------------------")
        print('n = '+str(n) + '4n = ' + str(4*n))
        print('n + 1 mod 7 = ' + str( (n+1) % 7))
        print('n + 1 mod 11 = ' + str( (n+1) % 11))
        print('n + 1 mod 13 = ' + str( (n+1) % 13))
        print('- interm = ' + str(interm))
        res = isqrt(interm)
        print("result p-q= " + str(res) + " at r = " + str(r))
        p = (r + res)/2
        q = n / p
        print("p = " + str(p))
        print("q = " + str(q))
        #print("k = " + str(k))
        if (p.is_integer() & q.is_integer()):
            print("DONE!")
            return(1)
    return(0)

def check_modlist(a,b,k,n):
    r = a * k + b

#    np1_modp = {}
#    for p in mod_p.keys():
#        np1_modp[int(p)] = (n+1) % int(p)
#        if (r % int(p)) in mod_p.get(str(int(p)),{-1:-1}).get(str(np1_modp[int(p)]),[-1,-1]):
#            continue
#        return
#    check_eq(r,n)

    # record results
#    for i in range(1,l+1):
#    	fplot.append(open('plot' + str(i), 'w+'))
    #if (((r % 7) in mod_p['7'][str((n+1) % 7)]) & ((r % 11) in mod_p['11'][str((n+1) % 11)]) & ((r % 13) in mod_p['13'][str((n+1) % 13)])):
        #check_eq(r,n)

    ret_eq = 0
    if ((r % 7) in mod_p['7'][str((n+1) % 7)]):
        ret_eq = check_eq(r,n)
    return(ret_eq)


def prep_check(s1,s2,s3,n):
    fp = open('eq.json', 'r')
    eq = json.load(fp)
    l = len(eq[s1 + s2 + '|' + s3]) / 2
    a = []; b = []; g = []; e = []; fplot = []

    print(n)
    for i in range(1,int(l)+1):
            #fplot.append(open('plot' + str(i), 'w+'))
            a.append(mpz(eq[s1 + s2 + '|' + s3]['a'+ str(i)]))
            b.append(mpz(eq[s1 + s2 + '|' + s3]['b'+ str(i)]))
            g.append(int(ceil((2 * ceil(sqrt(n)) - b[i-1]) / a[i-1])))
            e.append(int(ceil((sqrt(n**2 + 4*n - 1) - b[i-1]) / a[i-1])))

    fp.close()
    gs = sorted(enumerate(g) , key = lambda i:i[1])
    print (gs)
    print (e)
    n = mpz(n)


    m_e = min(e)
    m_g = min(g)
    while (m_g <= m_e):
        i = 0
        while (i < l):
            ret_modlist = check_modlist(a[i],b[i],g[i],n)
            if ret_modlist == 1 :
                return
            g[i] += 1
            if (g[i] >= m_e):
                ind_e = e.index(m_e)
                del e[ind_e]
                del g[ind_e]
                del a[ind_e]
                del b[ind_e]
                l = len(a)
                print(" deleting ind " + str(ind_e) + " e now : "),
                print(e)
                if (l == 0):
                    print("Ending...")
                    exit()
                m_e = min(e)
            i += 1


def start(n):
    n_100 = int(str(n)[-3])
    n_10 = int(str(n)[-2])
    n_1 = int(str(n)[-1])

    if ((n+1) % 3 == 0):
            s1 = '3'
    elif ((n+1) % 3 != 0):
            s1 = '3!'
    else:
            print ("Error")
            exit(1)

    if (n_1 == 3 or n_1 == 7):
            s3 = '0' + str(n_1)
            if (n_10 % 2 != 0):
                    s2 = ',4'
            elif (n_10 % 2 == 0):
                    s2 = ',4!'
            else:
                    print ("Error")
                    exit(1)

    elif (n_1 == 1 or n_1 == 9):
            s3 = str(n_10) + str(n_1)
            if (n_10 % 2 != 0):
                    if (n_100 % 2 != 0):
                            s2 = ',4'
                    elif (n_100 % 2 == 0):
                            s2 = ',4!'
                    else:
                            print ("Error")
                            exit(1)
            elif (n_10 % 2 == 0):
                    s2 = ''
            else:
                    print ("Error")
                    exit(1)
    else:
            print ("Error")
            exit(1)
    prep_check(s1,s2,s3,n)
    return


def main():
    tfp = open('time_opt2.log','a+')
    n = int(sys.argv[1])
    start_time = default_timer()
    start(n)
    Time = str(default_timer() - start_time)
    print( "Time: " +  Time )
    tfp.write("n = " + str(n) + "   length (digits): " + str(len(str(n))) + "   Time: " + Time + '\n')
    exit(0)

main()
