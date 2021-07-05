'''
Copyright Ali@C4C.KACST
'''
import sys
import gc
import util
import math
# from time import time
from operator import mul
from functools import reduce
from pathlib import Path
from tqdm.auto import tqdm
from gmpy2 import is_square
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

        if (len(self.h) != 0):
            self.num_p = len(self.h)

        if (self.num_p == None):
            raise Exception("Under dev. Please input" 
                            "number of primes manually")
            self._choose_num_p()

        if (len(self.h) == 0):
            self._choose_h()

        self.primes_used = self.h
        #print("primes:", self.primes_used)

        self.is_QR = [util.is_QR(self.n % p, p) for p in self.h]
        #print("is QR:", self.is_QR)
        #print("x= ", reduce(mul, self.h))
        #print("x bit length ", reduce(mul, self.h).bit_length())

        self.R_list = [self._load_R(h, n % h) for h in self.h]
        #print("Rh's:",  print(self.R_list))
        #print("Len's of Rh's:",  [len(R) for R in self.R_list])
        #print("Sizes of Rh's:",  [sys.getsizeof(R) for R in self.R_list])
        #print("Expected len of Rx:", reduce(mul, [len(R) for R in self.R_list]))
        # s_time = time()
        self.h, self.R = self._compute_Rx()

        #self.h, self.R = self._compute_Rx_np()
        #self.h, self.R = self._compute_Rx_opt4()
        #self.h, self.R = self._compute_Rx2(ind=(0,2))
        # time_diff = time() - s_time
        # print("compute_Rx took:", time_diff)
        # print(self._compute_Rx.__name__)
        # print(self._compute_Rx_np.__name__)
        #print(self._compute_Rx_opt4.__name__)

        #self.R = np.sort(self.R)
        self.R = sorted(self.R)
        # assert(self.h == self.h2)
        # for i in range(len(self.R)):
            # assert(self.R[i] == self.R2[i])
        #print("type Rx", type(self.R))
        #print("type Rx[0]", type(self.R[0]))
        #print("type h", type(self.h))
        # # print("Rx:", self.R)
        #print("Len of Rx:", len(self.R))
        #print("Size of Rx:", sys.getsizeof(self.R))

        self.c = self.n % self.h

        self._4n = 4 * self.n
        #self.sqrt_n = 2 * pow(self.n, 0.5) 
        self.sqrt_n = math.ceil(2 * pow(self.n, 0.5))
        sqrt_n_mod_h = self.sqrt_n % self.h
        self.b0_ind = int(np.searchsorted(self.R, sqrt_n_mod_h, side='left'))

        self.b0 = int(self.R[self.b0_ind])
        self.b = self.b0 - sqrt_n_mod_h
        self.k0 = (self.sqrt_n - sqrt_n_mod_h) // self.h
        # self.k0 = (self.sqrt_n) // self.h
        #print("Starting point (s0,b0):", (self.k0, self.b0))
        #self.R = self.R.tolist()
        #print("type Rx", type(self.R))
        #print("type Rx[0]", type(self.R[0]))
        #print("Len of Rx:", len(self.R))
        #print("Size of Rx:", sys.getsizeof(self.R))
        self.p_plus_q = None

    def _choose_num_p(self):
        #TODO: Fix (temporary measure)
        self.num_p = len(str(self.n))//2

    def _choose_h(self):
        primes = load_primes(self.primes_path)
        # Choose k for each prime
        for i, h in enumerate(primes):
            if (h == 2):
                if util.is_QR(self.n % 8, 8): #TODO: check Legendre
                    k = 12
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
            return [e((x0,x1)) for x0 in r1_list for x1 in r2_list]

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
    
    def _compute_Rx_np(self):
        assert(len(self.h) == len(self.R_list) and len(self.h) > 0)
        if (len(self.h) == 1):
            return self.h[0], sorted(self.R_list[0])

        def _compute_Rcrt(h1, h2, r1_list, r2_list):
            r2_arr = np.expand_dims(r2_list, axis=1)
            r1_arr = np.expand_dims(r1_list, axis=0)
            #print("arr1 type", r1_arr.dtype)
            inv_h1 = pow(h1, -1, h2)
            e = lambda x: ((inv_h1 * (x[1]-x[0])) % h2) * h1 + x[0]
            #return [e((x0,x1)) for x0 in r1_list for x1 in r2_list]
            return e((r1_arr, r2_arr)).flatten()

        h1 = self.h[0]
        h2 = self.h[1]
        assert(isinstance(h1, int) and isinstance(h2, int))
        r1_list = np.array(self.R_list[0], dtype=int)
        r2_list = np.array(self.R_list[1], dtype=int)
        x = h1 * h2
        Rx = _compute_Rcrt(h1, h2, r1_list, r2_list)

        for i in range(2, len(self.h)):
            Rx2 = _compute_Rcrt(self.h[i], x, np.array(self.R_list[i], dtype=int), Rx)
            del Rx
            Rx = Rx2
            del Rx2
            x *= self.h[i]

        return x, Rx

    def _compute_Rx2(self, ind=None):
        assert(len(self.h) == len(self.R_list) and len(self.h) > 0)
        if (len(self.h) == 1):
            return self.h[0], sorted(self.R_list[0])
        inv_dict = dict()
        x_list = [reduce(mul, self.h[:i]) for i in range(2,len(self.h))]

        def _compute_crt(h1, h2, r1, r2):
            if (h1, h2) in inv_dict:
                inv_h1 = inv_dict[(h1,h2)]
            else:
                inv_h1 = pow(h1, -1, h2)
                print("inv_h1 computed", (h1,h2))
                inv_dict[(h1,h2)] = inv_h1
            e = lambda x: ((inv_h1 * (x[1]-x[0])) % h2) * h1 + x[0]
            return e((r1, r2))

        def _compute_Rx_one(r_list):
            h1 = self.h[0]
            h2 = self.h[1]
            assert(isinstance(h1, int) and isinstance(h2, int))
            r1 = r_list[0]
            r2 = r_list[1]
            rx = _compute_crt(h1, h2, r1, r2)
            for i, r in enumerate(r_list[2:]): 
                h1 = self.h[i+2]
                rx = _compute_crt(h1, x_list[i], r, rx)
            return rx

        len_list = [len(R) for R in self.R_list]
        len_Rx = reduce(mul, len_list)
        if (ind == None):
            ind = (0, len_Rx)
        Rx = list()
        for i in range(ind[0], ind[1]):
            ind_list = [(i//reduce(mul, len_list[j+1:])) % len_list[j]
                    for j in range(len(len_list)-1)]
            ind_list.append(i % len_list[-1])
            assert(len(ind_list) == len(self.R_list))
            r_list = [self.R_list[i][ind_list[i]] for i in range(len(ind_list))]
            rx = _compute_Rx_one(r_list)
            Rx.append(rx)

        x = reduce(mul, self.h)
        return x, Rx

    def _compute_Rx2_np(self, ind=None):
        assert(len(self.h) == len(self.R_list) and len(self.h) > 0)
        if (len(self.h) == 1):
            return self.h[0], sorted(self.R_list[0])
        inv_dict = dict()
        x_list = [reduce(mul, self.h[:i]) for i in range(2,len(self.h))]

        def _compute_crt(h1, h2, r1, r2):
            if (h1, h2) in inv_dict:
                inv_h1 = inv_dict[(h1,h2)]
            else:
                inv_h1 = pow(h1, -1, h2)
                print("inv_h1 computed", (h1,h2))
                inv_dict[(h1,h2)] = inv_h1
            e = lambda x: ((inv_h1 * (x[1]-x[0])) % h2) * h1 + x[0]
            return e((r1, r2))

        def _compute_Rx_one(r_list):
            h1 = self.h[0]
            h2 = self.h[1]
            assert(isinstance(h1, int) and isinstance(h2, int))
            r1 = r_list[0]
            r2 = r_list[1]
            rx = _compute_crt(h1, h2, r1, r2)
            for i, r in enumerate(r_list[2:]): 
                h1 = self.h[i+2]
                rx = _compute_crt(h1, x_list[i], r, rx)
            return rx

        len_list = [len(R) for R in self.R_list]
        len_Rx = reduce(mul, len_list)
        if (ind == None):
            ind = (0, len_Rx)
        Rx = list()
        for i in range(ind[0], ind[1]):
            ind_list = [(i//reduce(mul, len_list[j+1:])) % len_list[j]
                    for j in range(len(len_list)-1)]
            ind_list.append(i % len_list[-1])
            assert(len(ind_list) == len(self.R_list))
            r_list = [self.R_list[i][ind_list[i]] for i in range(len(ind_list))]
            rx = _compute_Rx_one(r_list)
            Rx.append(rx)

        x = reduce(mul, self.h)
        return x, Rx

    def _compute_Rx_opt(self):
        # 1. prep initial list (by taking one list and expanding to x)
        # 2. check if elements of the list mod h_i are in R_list_i
#        Rx_init = list()
#        x = reduce(mul, self.h)
#        for a in self.R_list[0]:
#            Rx_init.extend([a + self.h[0]*i for i in range(0, x//self.h[0])])
#        #print("init Rx:", Rx_init)
#        #print("init Rx:", len(Rx_init))
#        Rx = Rx_init.copy()
#        for j, r in enumerate(Rx_init):
#            for i in range(1, len(self.R_list)):
#                if r % self.h[i] not in self.R_list[i]:
#                    del Rx[Rx.index(r)]
#                    break
        def process_r(r, h):
            a = r
            delete_count = 0
            a_list = list()
            for i in range(0, x//h):
                a_list.append(a)
                a += h
            i = 0
            while i < len(a_list):
                for j in range(len(self.R_list)-2, -1, -1):
                    if a_list[i] % self.h[j] not in self.R_list[j]:
                        del a_list[i-delete_count]
                        delete_count += 1
                        break
                i += 1
            return a_list
        x = reduce(mul, self.h)
        Rx = list()
        for r in self.R_list[-1]:
            Rx.extend(process_r(r, self.h[-1]))
        return x, Rx

    def _compute_Rx_opt2(self):
        # 1. prep initial list (by taking one list and expanding to x)
        # 2. check if elements of the list mod h_i are in R_list_i
        def process_r(r, h):
            a = r
            for i in range(0, x//h):
                notfound = False
                for j in range(1, len(self.R_list)):
                    if a % self.h[j] not in self.R_list[j]:
                        notfound = True
                        break
                if not notfound:
                    Rx.append(a)
                a += h
        x = reduce(mul, self.h)
        Rx = list()
        for r in self.R_list[0]:
            process_r(r, self.h[0])
        return x, Rx

    def _compute_Rx_opt3(self):
        # 1. prep initial list (by taking one list and expanding to x)
        # 2. check if elements of the list mod h_i are in R_list_i
        assert(sum(self.is_QR) == len(self.is_QR))
        def process_r(r, h):
            a = r
            #print("r:",r)
            for i in range(0, x//h):
                notfound = False
                #print("a", a, "i", i),
                for j in range(len(self.R_list)-1, -1, -1):
                    if a % self.h[j] not in self.R_list[j]:
                        notfound = True
                        break
                if not notfound:
                    #print("_____"),
                    Rx.append(a)
                    index_list.append(i)
                a += h
        x = reduce(mul, self.h)
        x_1 = reduce(mul, self.h[:-1])
        Rx = list()
        index_list = list()
        #for r in self.R_list[-1]:
        process_r(self.R_list[-1][0], self.h[-1])
        for r in self.R_list[-1][1:]:
            for i in index_list:
                Rx.append(r + self.h[-1]*((r+i)%x_1))
                #Rx.append((r + self.h[-1]*r)%x)

        return x, Rx

    def _compute_Rx_opt4(self):
        #assert(sum(self.is_QR) == len(self.is_QR))
        def process_r(r, h):
            S = list()
            a = r
            #print("r:",r)
            for i in range(0, x//h):
                notfound = False
                #print("a", a, "i", i),
                for j in range(len(self.R_list)-2, -1, -1):
                    if a % self.h[j] not in self.R_list[j]:
                        notfound = True
                        break
                if not notfound:
                    #print("_____"),
                    S.append(a)
                a += h
            return S
        x = reduce(mul, self.h)
        x_1 = x // self.h[-1]
        Rx = list()
        S_init = process_r(0, self.h[-1])
        #print("init_S", S_init)

        len_init_Rx = len(S_init)
        x_1_mod_H = x_1 % self.h[-1]
        #print("x/H % H", x_1_mod_H)
        ri_list = [(x_1_mod_H*i) % self.h[-1] for i in range(1, self.h[-1])]
        #print("ri_list", ri_list)
        for r_ind, r in enumerate(self.R_list[-1]):
            if (r == 0):
                Rx.extend(S_init)
                continue
            i = ri_list.index(r) + 1
            ad = i*x_1
            #print("ad", ad)
            for j in range(len_init_Rx):
                #Rx.append((r + self.h[-1]*r)%x)
                Rx.append((S_init[j] + ad)%x)
        #print("Rx,", Rx)

        return x, Rx

    def _search_step_j(self, i, j):
        r = self.h * (self.k0 + i) + self.R[j]
        #if (r != None and r > 121477995219678):
            #print(self.R[j-10:j])
            #print(type(self.R[j-1]))
            #raise Exception("skipped solution!")
        #return util.isSquare(r**2 - self._4n), r
        return is_square(r**2 - self._4n), r
        
    def _search_step_i(self, i):
        if (i == 0):
            j = self.b0_ind
        else:
            j = 0
        while (j < len(self.R)):
        # for j in range(len(self.R)):
            res, r = self._search_step_j(i, j)
            # if j == 0:
                # print("res, r", res, r)
            if res:
                # print("res, r", res, r)
                return res, (j, r)
            j += 1
        return res, (j, r)

    def search(self):
        i = 0
        with tqdm(desc="Search", 
                  total=int(((self.n/3)+3))//(self.h*len(self.R)),
                  disable=not self.progress) as pbar:
            # search_start_time = time()
            while(i < int((self.n/3) + 3)):  # TODO: Ask: is this limit exact or floor?
                res, r = self._search_step_i(i)
                if (res):
                    # search_end_time = time()
                    pbar.close()
                    # print("Search took:", search_end_time - search_start_time)
                    self.p_plus_q = r[1]
                    #print(self.R[r[0]-10:r[0]])
                    #print(type(self.R[r[0]-1]))
                    return i, r
                #if (r != None and r[1] > 121477995219678):
                   #print("Skipped solution!!:", i, r)
                   # return i, r
                i += 1
                pbar.update(1)

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
    # pqs1 = PQSieve(1, h=[2, 3, 5])
    # pqs2 = PQSieve(1, h=[2**2, 3, 5])
    # pqs3 = PQSieve(1, h=[2, 3])
    # pqs4 = PQSieve(1, h=[3, 5, 7, 11])
    #res1 = pqs1.search()
    #print(res1)

    #Experiment 2 (h=2^12)
    #pqs2 = PQSieve(12759908025574684369, h=[2**12])
    #res2 = pqs2.search()
    #print(res2)

    #Experiment 3 (h1=2^12, h2=3^3)
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
    pqs4 = PQSieve(12759908025574684369, h=[], num_p=7)
    res4 = pqs4.search()
    print(res4)

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
