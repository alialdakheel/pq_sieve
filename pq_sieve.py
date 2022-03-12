'''
Copyright Ali@C4C.KACST
'''
import sys
import gc
import util
import math
from gmpy2 import is_square
# from time import time
from operator import mul
from functools import reduce
from pathlib import Path
from tqdm.auto import tqdm
import numpy as np
from precompute import precompute_c, is_precomputed, load_primes

'''
* p+q Sieve Factoring
** 1. compute g=ceil(2sqrt(n)), and load p+q relations (R(c,h) or R(c,x))
** 2. Search for p+q by finding r where sqrt(r^2 - 4n) is an integer; where r in [g,n/3+3]
'''
class PQSieve():
    def __init__(self,
                 n,
                 num_p=None,
                 h=[],
                 precompute_dir=Path('precompute_store/'),
                 primes_path="primes.txt",
                 progress=True
                 ):
        assert(isinstance(n, int) and isinstance(h, list))
        self.n = n
        self.h = h
        self.num_p = num_p
        self.p_dir = precompute_dir
        self.primes_path = primes_path
        self.progress = progress
        self.total_i = 0

        if (len(self.h) != 0):
            self.num_p = len(self.h)

        if (self.num_p == None):
            raise Exception("Under dev. Please input" 
                            "number of primes manually")
            self._choose_num_p()

        if (len(self.h) == 0):
            self._choose_h()

        self.primes_used = self.h

        self.is_QR = [util.is_QR(self.n % p, p) for p in self.h]

        self.R_list = [self._load_R(h, n % h) for h in self.h]

        self._4n = 4 * self.n
        self.sr = pow(self.n, 0.5)
        # self.bound = (101/10) * self.sr # Bound for p+q
        self.bound_i = (101/10) * self.sr
        self.sqrt_n = math.ceil(2 * self.sr)

        self.h, self.R = self._compute_Rx()
        self.R_size = len(self.R)

        self.R = sorted(self.R)

        self.c = self.n % self.h

        sqrt_n_mod_h = self.sqrt_n % self.h
        self.b0_ind = int(np.searchsorted(self.R, sqrt_n_mod_h, side='left'))
        self.b0 = int(self.R[self.b0_ind])
        self.b = self.b0 - sqrt_n_mod_h
        self.k0 = (self.sqrt_n - sqrt_n_mod_h) // self.h
        self.p_plus_q = None

    def _choose_num_p(self):
        #TODO: (temporary measure)
        self.num_p = len(str(self.n))//2

    def _choose_h(self):
        primes = load_primes(self.primes_path)
        # Choose k for each prime
        for i, h in enumerate(primes):
            if (h == 2):
                if self.n % 8 == 1:
                    k = 6
                else:
                    k = 3
            else:
                if util.is_QR(self.n % h, h):
                    if (h == 3):
                        k = 3
                    elif (h == 5):
                        k = 2
                    else:
                        continue
                else:
                    k = 1
            self.h.append(h**k)
            if (len(self.h) >= self.num_p):
                break

    def _load_R(self, h, c):
        if is_precomputed(h, c, self.p_dir):
            return util.load_json(h, c, self.p_dir)
        else:
            R = precompute_c(c, h)
            util.save_json_c(h, c, R, self.p_dir)
            return R

    def _compute_Rx(self):
        assert(len(self.h) == len(self.R_list) and len(self.h) > 0)
        if (len(self.h) == 1):
            return self.h[0], sorted(self.R_list[0])

        def _compute_Rcrt(h1, h2, r1_list, r2_list):
            inv_h1 = pow(h1, -1, h2)
            e = lambda x: ((inv_h1 * (x[1]-x[0])) % h2) * h1 + x[0]
            return [
                    e((x0,x1)) for x0 in r1_list for x1 in r2_list
                    # if e((x0, x1)) <= self.bound
            ]

        h1 = self.h[0]
        h2 = self.h[1]
        assert(isinstance(h1, int) and isinstance(h2, int))
        # r1_list = self.R_list[0]
        # r2_list = self.R_list[1]
        x = h1 * h2
        Rx = _compute_Rcrt(h1, h2, self.R_list[0], self.R_list[1])

        for i in range(2, len(self.h)):
            Rx2 = _compute_Rcrt(self.h[i], x, self.R_list[i], Rx)
            del Rx
            Rx = Rx2
            del Rx2
            x *= self.h[i]

        return x, Rx

    def _search_step_j(self, i, j):
        r = self.h * (self.k0 + i) + self.R[j]
        return is_square(r**2 - self._4n), r
        
    def _search_step_i(self, i):
        if (i == 0):
            j = self.b0_ind
        else:
            j = 0
        while (j < len(self.R)):
            res, r = self._search_step_j(i, j)
            if res:
                return res, (j, r)
            j += 1
        return res, (j, r)

    def search(self):
        i = 0
        with tqdm(desc="Search", 
                  total=int(((self.n/3)+3))//(self.h*len(self.R)),
                  disable=not self.progress) as pbar:
            while(i < self.bound_i):  # TODO: Check bound ? 
                res, r = self._search_step_i(i)
                if (res):
                    pbar.close()
                    self.total_i = i
                    self.last_j = r[0]
                    self.p_plus_q = r[1]
                    return i, r
                i += 1
                pbar.update(1)
            raise("Search did not find a solution")


    def factors(self):
        assert(self.p_plus_q)
        sqrt_r = pow(self.p_plus_q**2 - self._4n, 0.5)
        p = (self.p_plus_q + sqrt_r) // 2
        q = (self.p_plus_q - sqrt_r) // 2
        return int(p), int(q)

if __name__ == "__main__":
    #Experiment old (defaults)
    #pqs_old = PQSieve(800694907089021864656603)
    #res_old = pqs_old.search()

    #Experiment 1 (defaults) 20 digit, 64 bit number
    #pqs1 = PQSieve(12759908025574684369, h=[2, 3, 5, 17, 23, 29])
    #res1 = pqs1.search()
    #print(res1)

    #Experiment 2 (h=2^12)
    # pqs2 = PQSieve(12759908025574684369, h=[2**12])
    # res2 = pqs2.search()
    # print(res2)
    # pqs2 = PQSieve(12759908025574684369, h=[2**6])
    # res2 = pqs2.search()
    # print(res2)
    # print("Rx" , pqs2.R)

    #Experiment 3 (h1=2^12, h2=3^3)
    pqs3 = PQSieve(12759908025574684369, h=[2**6, 3**3])
    res3 = pqs3.search()
    print(res3)
    print("Rx" , pqs3.R)
    # pqs3 = PQSieve(12759908025574684369, h=[2**12, 3**4, 5**3, 7])
    # res3 = pqs3.search()
    # print(res3)
    # del pqs3
    # pqs3 = PQSieve(12759908025574684369, num_p=7)
    # res3 = pqs3.search()
    # print(res3)

    # Experiment 3 (h1=2^12, h2=3^3)
    # pqs3 = PQSieve(12759908025574684369, h=[2, 3, 5, 7, 11])
    #res3 = pqs3.search()
    #print(res3)

    #Experiment 4 (num_p=8)
    # pqs4 = PQSieve(12759908025574684369, h=[], num_p=7)
    # res4 = pqs4.search()
    # print(res4)

    #Experiment 5 (num_p=9) 21 digit, 68 bit number
    #pqs5 = PQSieve(223710178181483884087, h=[], num_p=4)
    #res5 = pqs5.search()
    #print(res5)
    
    #Experiment 5 (num_p=8) 21 digit, 68 bit number
    # pqs5 = PQSieve(223710178181483884087, h=[2**12, 3**3, 5, 7, 11, 13, 17])
    #res5 = pqs5.search()
    #print(res5)

    #Experiment 6 (custom) 22 digit, 72 bit number
    # pqs6 = PQSieve(4014363189286667855933, h=[2**3, 3, 5, 17, 19, 23, 31, 37, 41, 43])
    # pqs6 = PQSieve(4014363189286667855933, h=[2**3, 3, 5, 7**2, 17, 19, 23, 31, 37])
    # pqs6 = PQSieve(4014363189286667855933, h=[2**3, 3, 5, 17, 19, 23, 31, 37])
    # res6 = pqs6.search()
    # print(res6)
    # del pqs6
    # pqs6 = PQSieve(4014363189286667855933, num_p=9)
    # res6 = pqs6.search()
    # print(res6)

    #Experiment 6 (num_p=6) 22 digit, 72 bit number
    # pqs6 = PQSieve(4014363189286667855933, h=[], num_p=16)
    #res6 = pqs6.search()
    #print(res6)

    #Experiment 7 (num_p=9) 23 digit, 76 bit number
    #pqs7 = PQSieve(52273100668689816612043, h=[], num_p=9)
    #res7 = pqs7.search()
    #print(res7)

    #Experiment 8 (num_p=9) 25 digit, 80 bit number
    #pqs8 = PQSieve(1000424515683925933626023, h=[], num_p=9)
    #res8 = pqs8.search()
    #print(res8)

    #Experiment 9 (num_p=10) 26 digit, 84 bit number
    #pqs9 = PQSieve(13264984799917245005244533, h=[], num_p=10)
    #res9 = pqs9.search()
    #print(res9)

    #Experiment 10 (num_p=10) 28 digit, 92 bit number
    #pqs10 = PQSieve(3677169269011909330112649617, h=[], num_p=8)
    #res10 = pqs10.search()
    #print(res10)

    #Experiment 10 (custom) 28 digit, 92 bit number
    # pqs10 = PQSieve(3677169269011909330112649617, h=[2**12, 3, 5, 13, 23, 31, 43, 47])
    # res10 = pqs10.search()
    # print(res10)

    #Experiment 11 (num_p=11) 29 digit, 96 bit number
    #pqs11 = PQSieve(62821100886317431913009499013, h=[], num_p=11)
    #res11 = pqs11.search()
    #print(res11)

    #Experiment 12 (num_p=11) 31 digit, 100 bit number
    #pqs12 = PQSieve(1026521762973406557162751475101, h=[], num_p=10)
    #res12 = pqs12.search()
    #print(res12)

    #Experiment 12 (custom) 31 digit, 100 bit number
    # pqs12 = PQSieve(1026521762973406557162751475101, h=[2**12, 3**3, 5**2, 11, 13, 17, 23, 29])
    # res12 = pqs12.search()
    # print(res12)

    #Experiment RSA-110
    #pqs_rsa1 = PQSieve(35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667, h=[], num_p=10)

    #Experiment RSA-110
    #pqs_rsa1 = PQSieve(35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667, h=[2**12, 3**3, 5, 7, 11, 13, 17, 19])
