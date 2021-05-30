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
import multiprocessing


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

        self.c = n % h

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

        self.queue = multiprocessing.Queue()

    def _search_step_j(self, i, j):
        r = self.h * (self.k0 + i) + self.R[j]
        return is_square(r**2 - self._4n), r

    def _search_step_mp(self, j):
        i = 0
        with tqdm(desc=f"Search ({j})", disable=(j!=0), position=j+1, total=int(((self.n/3)+3)-self.a_0)//self.h) as pbar:
            while(i < int((3 * self.n) / 3)):  # TODO: Ask: is this limit exact or floor?
                res, r = self._search_step_j(i, j)
                if(res):
                    self.queue.put((i, r))
                    break
                i += 1
                pbar.update(1)
            pbar.close()
        
    def search(self):
        p_list = [multiprocessing.Process(target=self._search_step_mp, args=(j,)) for j in range(len(self.R))]
        for p in p_list:
            p.start()

        res = self.queue.get()
        print("result:", res)
        for p in p_list:
            p.terminate()

if __name__ == "__main__":
    #Experiment old (defaults)
    #pqs_old = PQSeive(800694907089021864656603)
    #res_old = pqs_old.search()


    #Experiment 1 (defaults)
    pqs1 = PQSeive(12759908025574684369)
    #res1 = pqs1.search()
    #print(res1)

    #Experiment 2 (defaults)
    pqs2 = PQSeive(12759908025574684369, h=2**12)
    #res2 = pqs2.search()
    #print(res2)
