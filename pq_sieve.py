'''
Copyright Ali@C4C.KACST
'''
import sys
import util
import math
from time import time
from operator import mul
from functools import reduce
from pathlib import Path
from tqdm.auto import tqdm
from gmpy2 import is_square
from precompute import precompute_c, is_precomputed, load_primes

'''
* p+q Sieve Factoring
** 1. compute g=ceil(2sqrt(n)), and load p+q relations (R(c,h) or R(c,x))
** 2. Search for p+q by finding r where sqrt(r^2 - 4n) is an integer; where r in [g,n/3+3]
'''
class PQSieve():
    def __init__(self, n, h=[7], num_p=100,
            precompute_dir=Path('precompute_store/'), primes_path="primes.txt"):
        assert(isinstance(n, int) and isinstance(h, list))
        self.n = n
        self.h = h
        if len(self.h) == 0:
            self.h = load_primes(primes_path)[0:num_p]

        self.p_dir = precompute_dir

        self.R_list = [self._load_R(h, n % h) for h in self.h] 
        print("Len's of Rh's:",  [len(R) for R in self.R_list])
        print("Sizes of Rh's:",  [sys.getsizeof(R) for R in self.R_list])
        print("Expected len of Rx:", reduce(mul, [len(R) for R in self.R_list]))
        s_time = time()
        self.h, self.R = self._compute_Rx()
        time_diff = time() - s_time
        print("compute_Rx took:", time_diff)
        print("Len of Rx:", len(self.R))
        print("Size of Rx:", sys.getsizeof(self.R))

        self.c = self.n % self.h

        self._4n = 4 * self.n
        self.sqrt_n = 2 * pow(self.n, 0.5) 
        self.a_0 = min(self.R)
        self.k0 = math.ceil((self.sqrt_n - self.a_0) / self.h)

    def _load_R(self, h, c):
        if is_precomputed(h, c, self.p_dir):
            return util.load_json(h, c, self.p_dir)
        else:
            R = precompute_c(c, h)
            util.save_json_c(h, c, R, self.p_dir)
            return R

    def _compute_Rx(self):
        assert(len(self.h) == len(self.R_list) and len(self.h) > 0)
        if len(self.h) == 1:
            return self.h[0], sorted(self.R_list[0])

        h1 = self.h.pop()
        h2 = self.h.pop()
        assert(isinstance(h1, int) and isinstance(h2, int))
        r1_list = self.R_list.pop()
        r2_list = self.R_list.pop()

        self.h.append(h1 * h2)
        self.R_list.append(util.compute_Rcrt(h1, h2, r1_list, r2_list))
        del h1; del h2; del r1_list; del r2_list
        return self._compute_Rx()

    def _search_step_j(self, i, j):
        r = self.h * (self.k0 + i) + self.R[j]
        return is_square(r**2 - self._4n), r
        
    def _search_step_i(self, i):
        for j in range(len(self.R)):
            res, r = self._search_step_j(i, j)
            if res:
                return res, (j , r)
        return False, None

    def search(self):
        i = 0
        with tqdm(desc="Search",
                total=int(((self.n/3)+3)-self.a_0)//self.h) as pbar:
            while(i < int((3 * self.n) / 3)):  # TODO: Ask: is this limit exact or floor?
                res, r = self._search_step_i(i)
                if(res):
                    return i, r
                i += 1
                pbar.update(1)

if __name__ == "__main__":
    #Experiment old (defaults)
    #pqs_old = PQSieve(800694907089021864656603)
    #res_old = pqs_old.search()


    #Experiment 1 (defaults)
    #pqs1 = PQSieve(12759908025574684369)
    #res1 = pqs1.search()

    #Experiment 2 (h=2^12)
    #pqs2 = PQSieve(12759908025574684369, h=[2**12])
    #res2 = pqs2.search()
    #print(res2)

    #Experiment 3 (h1=2^12, h2=3^3)
    #pqs3 = PQSieve(12759908025574684369, h=[2**12, 3**3])
    #res3 = pqs3.search()
    #print(res3)

    #Experiment RSA-110
    pqs_rsa1 = PQSieve(35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667, h=[], num_p=9)
