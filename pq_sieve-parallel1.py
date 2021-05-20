'''
Copyright Ali@C4C.KACST
'''
import util
import math
from pathlib import Path
from tqdm.auto import tqdm
from sqlitedict import SqliteDict
from gmpy2 import is_square
from precompute import precompute_c
import multiprocessing


'''
* p+q Sieve Factoring
** 1. compute g=ceil(2sqrt(n)), and load p+q relations (R(c,h) or R(c,x))
** 2. Search for p+q by finding r where sqrt(r^2 - 4n) is an integer; where r in [g,n/3+3]
'''
class PQSeive():
    def __init__(self, n, h=7, precompute_path=Path('precompute/mod_p_store.sqlite')):
        self.n = n
        self.h = h
        self.p_path = precompute_path

        self.c = n % h

        with SqliteDict(self.p_path) as store_dict:
            try:
                self.R = store_dict[str(self.h)][self.c]
            except KeyError:
                print(f"Precomputed values not found for c={self.c}, h={self.h}, computing on-the-fly...")
                self.R = precompute_c(self.c, self.h)

        self.pool = multiprocessing.Pool()

        self._4n = 4 * self.n
        self.sqrt_n = 2 * math.ceil(pow(n, 0.5)) 
        self.a_0 = min(self.R)
        self.k0 = math.ceil((self.sqrt_n - self.a_0) / self.h)

    def _search_step_j(self, i, j):
        r = self.h * (self.k0 + i) + self.R[j]
        return is_square(r**2 - self._4n), r

    def _search_step_mp(self, i):
        results = self.pool.starmap(self._search_step_j, zip([i] * len(self.R), range(len(self.R))))
        for j, (res, r) in enumerate(results):
            if res:
                return res, (j, r)
        return False, None
        
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
                #res, r = self._search_step_i(i)
                res, r = self._search_step_mp(i)
                if(res):
                    return i, r
                i += 1
                pbar.update(1)

if __name__ == "__main__":
    #Experiment old (defaults)
    #pqs_old = PQSeive(800694907089021864656603)
    #res_old = pqs_old.search()


    #Experiment 1 (defaults)
    pqs1 = PQSeive(12759908025574684369)
    res1 = pqs1.search()
    print(res1)

    #Experiment 2 (defaults)
    #pqs2 = PQSeive(12759908025574684369, h=2**12)
    #res2 = pqs2.search()
    #print(res2)
