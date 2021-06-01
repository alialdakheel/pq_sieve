#!/usr/bin/env python

import sys
from pathlib import Path
from tqdm.auto import tqdm
import util

store_dir = "precompute_store/"

'''
    Precompute using num_p primes from a list of primes (loaded from file)
'''
def precompute(num_p, offset=0, primes_path="primes.txt", store_dir=store_dir):
    Path(store_dir).mkdir(exist_ok=True)

    pfp = open(primes_path,'r') #prime file pointer to a list of primes

    # prepare prime list
    primes = pfp.read().split()
    #del primes[0:3] # delete first three primes namely [2,3,5]
    del primes[0] # delete first prime (2)

    for p in tqdm(primes[offset:num_p], desc="Precomputing"):
        p = int(p)
        rc_dict = precompute_p(p)
        util.save_json(p, rc_dict, store_dir)

def precompute_p(p, k=1):
    pk = p**k
    rc_dict = {c: set() for c in range(1, pk) if c % p != 0}
    for i in tqdm(range(1, pk),
            desc=f"Computing R(p={p},k={k})", leave=False):
        for j in range(i, pk):
            prod = (i*j) % pk
            if prod % p == 0:
                continue
            s = (i+j) % pk
            rc_dict[prod].add(s)
    return {c:sorted(list(r_set)) for c, r_set in rc_dict.items()}

def is_precomputed(p, c, store_dir=store_dir):
    path = Path(store_dir)/f'{p}_{c}_store.json'
    return path.is_file()

def precompute_c(c, p):
        if isinstance(p, list):
            c_list = [c % p_i for p_i in p]
            R_list = [precompute_c(c_i, p_i) for c_i, p_i in zip(c_list, p)]
            x = reduce(mul, p)
            raise Exception("Under dev...")
        elif isinstance(p, int):
            mod_p = list()
            for i in tqdm(range(1, p), desc=f"Computing R(p={p},c={c})"):
                for j in range(i, p):
                    prod = (i*j) % p
                    s = (i+j) % p
                    #print("i", i, "j", j, "p", prod , "s", s)
                    if prod != c or s in mod_p:
                        continue
                    mod_p.append(s)
            return sorted(set(mod_p))
        else:
            raise Exception("input p has unknown type")

if __name__ == "__main__":
    precompute(int(sys.argv[1]))

