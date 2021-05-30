'''
Copyright Ali@C4C.KACST
'''
import util
import math
from operator import mul
from functools import reduce
from pathlib import Path
from tqdm.auto import tqdm
from sqlitedict import SqliteDict
from gmpy2 import is_square
from precompute import precompute_c

'''
* p+q Sieve Factoring
** 1. compute g=ceil(2sqrt(n)), and load p+q relations (R(c,h) or R(c,x))
** 2. Search for p+q by finding r where sqrt(r^2 - 4n) is an integer; where r in [g,n/3+3]
'''
class PQSeive():
    def __init__(self, n, h=7, precompute_path=Path('precompute/mod_p_store.sqlite')):
        self.n = n
        if isinstance(h, list):
            self.h = reduce(mul, h)
        elif isinstance(h, int):
            self.h = h
        else:
            raise Exception("input h has unknown type")
        self.p_path = precompute_path

        self.c = self.n % self.h

        with SqliteDict(self.p_path) as store_dict:
            try:
                self.R = store_dict[str(self.h)][self.c]
            except KeyError:
                print(f"Precomputed values not found for c={self.c}, h={self.h}, computing on-the-fly...")
                self.R = precompute_c(self.c, self.h)
                store_dict[str(self.h)] = {self.c: self.R}
                store_dict.commit()

        self._4n = 4 * self.n
        self.sqrt_n = 2 * pow(self.n, 0.5) 
        self.a_0 = min(self.R)
        self.k0 = math.ceil((self.sqrt_n - self.a_0) / self.h)

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
        with tqdm(desc="Search", total=int(((self.n/3)+3)-self.a_0)//self.h) as pbar:
        # with tqdm(desc="Search") as pbar:
            while(i < int((3 * self.n) / 3)):  # TODO: Ask: is this limit exact or floor?
                #print(i)
                res, r = self._search_step_i(i)
                if(res):
                    return i, r
                i += 1
                pbar.update(1)

if __name__ == "__main__":
    #Experiment old (defaults)
    #pqs_old = PQSeive(800694907089021864656603)
    #res_old = pqs_old.search()


    #Experiment 1 (defaults)
    #pqs1 = PQSeive(12759908025574684369)
    #res1 = pqs1.search()

    #Experiment 2 (h=2^12)
    #pqs2 = PQSeive(12759908025574684369, h=2**12)
    #res2 = pqs2.search()

    #Experiment 3 (h1=2^12, h2=3^3)
    pqs3 = PQSeive(12759908025574684369, h=[2**12, 3**3])
    #res3 = pqs3.search()
