'''
Copyright Ali@C4C.KACST
'''

import util
import numpy as np
from operator import mul
from functools import reduce
from tqdm.auto import tqdm
from precompute import precompute_c, is_precomputed, load_primes

class RX():
    def __init__(self, n, num_p=None, h=list(),
                 strategy=0,
                 precompute_dir='precompute_store/',
                 primes_path="primes.txt",
                 progress=True
                 ):
        self.n = n
        self.num_p = num_p
        self.h = h
        self.strategy = strategy
        self.p_dir = precompute_dir
        self.primes_path = primes_path
        self.progress = progress

        if not self.num_p:
            raise Exception("Under dev. Please input" 
                            "number of primes manually")
            self._choose_num_p()
        self._choose_h()
        self.primes_used = self.h
        self.is_QR = [util.is_QR(self.n % p, p) for p in self.h]
        self.R_list = [self._load_R(h, n % h, progress=self.progress)
                       for h in self.h]

    def _choose_num_p(self):
        #TODO: Fix (temporary measure)
        self.num_p = len(str(self.n))//2

    def _choose_h(self):
        primes = load_primes(self.primes_path)
        # Choose k for each prime
        self.h = list()
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

    def _load_R(self, h, c, progress=False):
        if is_precomputed(h, c, self.p_dir):
            return util.load_json(h, c, self.p_dir)
        else:
            R = precompute_c(c, h, progress=progress)
            util.save_json_c(h, c, R, self.p_dir)
            return R

    def _compute_Rx(self):
        """
        Compute R(c,x) using CRT as in paper
        """
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

        for i in tqdm(range(2, len(self.h)),
                      desc="Computing Rx",
                      disable=not self.progress):
            Rx2 = _compute_Rcrt(self.h[i], x, self.R_list[i], Rx)
            del Rx
            Rx = Rx2
            del Rx2
            x *= self.h[i]

        return x, Rx
    
    def _compute_Rx_np(self, dtype=object):
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
        r1_list = np.array(self.R_list[0], dtype=dtype)
        r2_list = np.array(self.R_list[1], dtype=dtype)
        x = h1 * h2
        Rx = _compute_Rcrt(h1, h2, r1_list, r2_list)

        for i in tqdm(range(2, len(self.h)),
                      desc="Computing Rx",
                      disable=not self.progress):
            Rx2 = _compute_Rcrt(self.h[i], x, self.R_list[i], Rx)
            Rx2 = _compute_Rcrt(self.h[i], x, np.array(self.R_list[i], dtype=dtype), Rx)
            del Rx
            Rx = Rx2
            del Rx2
            x *= self.h[i]

        return x, Rx

    def Rx_gen(self, ind=None):
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
        for i in range(ind[0], ind[1]):
            ind_list = [(i//reduce(mul, len_list[j+1:])) % len_list[j]
                    for j in range(len(len_list)-1)]
            ind_list.append(i % len_list[-1])
            assert(len(ind_list) == len(self.R_list))
            r_list = [self.R_list[i][ind_list[i]] for i in range(len(ind_list))]
            rx = _compute_Rx_one(r_list)
            yield rx

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
        for i in tqdm(range(ind[0], ind[1]),
                      desc="Computing Rx",
                      disable=not self.progress):
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

    def _compute_Rx_opt2(self):
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

    def _compute_Rx_opt4(self):
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
