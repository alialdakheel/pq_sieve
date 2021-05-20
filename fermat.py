'''
Copyright Ali@C4C.KACST
'''
import util
import math
from pathlib import Path
from tqdm.auto import tqdm
from sqlitedict import SqliteDict
from gmpy2 import is_square

'''
* Fermat Factoring
** 1. compute g=ceil(2sqrt(n))
** 2. Search for p+q by finding r where sqrt(r^2 - 4n) is an integer; where r in [g,n/3+3]
'''
class Fermat():
    def __init__(self, n):
        self.n = n

        self._4n = 4 * self.n
        self.sqrt_n = 2 * math.ceil(pow(n, 0.5)) 

    def _search_step_j(self, i, j):
        r = self.h * (self.k0 + i) + self.R[j]
        return is_square(r**2 - self._4n), r
        
    def _search_step_i(self, i):
        for j in range(len(self.R)):
            res, r = self._search_step_j(i, j)
            r = self.h * (self.k0 + i) + self.R[j]
            return is_square(r**2 - self._4n), r
            if res:
                return res, (j , r)
        return False, None

    def _check_condition(self, i):
        r = self.sqrt_n + i
        return is_square(r**2 - self._4n), r

    def search(self):
        i = 0
        with tqdm(desc="Search", total=int((self.n/3)+3)) as pbar:
        # with tqdm(desc="Search") as pbar:
            while(i < self.n):  # TODO: Ask: is this limit exact or floor?
                #print(i)
                res, r = self._check_condition(i)
                if(res):
                    return i, r
                i += 1
                pbar.update(1)
        print("Not found!")

if __name__ == "__main__":
    # pqs = Fermat(800694907089021864656603)
    pqs = Fermat(12759908025574684369)
    res = pqs.search()
