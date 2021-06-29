import json
from gmpy2 import invert
from pathlib import Path

'''
From: https://stackoverflow.com/questions/2489435/check-if-a-number-is-a-perfect-square/45724520
'''
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

'''
    From: https://stackoverflow.com/questions/2489435/check-if-a-number-is-a-perfect-square
'''
def isSquare(n):
    ## Trivial checks
    if type(n) != int:  ## integer
        return False
    if n < 0:      ## positivity
        return False
    if n == 0:      ## 0 pass
        return True

    ## Reduction by powers of 4 with bit-logic
    while n&3 == 0:    
        n=n>>2

    ## Simple bit-logic test. All perfect squares, in binary,
    ## end in 001, when powers of 4 are factored out.
    if n&7 != 1:
        return False

    if n==1:
        return True  ## is power of 4, or even power of 2


    ## Simple modulo equivalency test
    c = n%10
    if c in {3, 7}:
        return False  ## Not 1,4,5,6,9 in mod 10
    if n % 7 in {3, 5, 6}:
        return False  ## Not 1,2,4 mod 7
    if n % 9 in {2,3,5,6,8}:
        return False  
    if n % 13 in {2,5,6,7,8,11}:
        return False  

    ## Other patterns
    if c == 5:  ## if it ends in a 5
        if (n//10)%10 != 2:
            return False    ## then it must end in 25
        if (n//100)%10 not in {0,2,6}: 
            return False    ## and in 025, 225, or 625
        if (n//100)%10 == 6:
            if (n//1000)%10 not in {0,5}:
                return False    ## that is, 0625 or 5625
    else:
        if (n//10)%4 != 0:
            return False    ## (4k)*10 + (1,9)


    ## Babylonian Algorithm. Finding the integer square root.
    ## Root extraction.
    s = (len(str(n))-1) // 2
    x = (10**s) * 4

    A = {x, n}
    while x * x != n:
        x = (x + (n // x)) >> 1
        if x in A:
            return False
        A.add(x)
    return True

'''
    From: https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
'''
def find_nearest(array, value):
    idx = np.searchsorted(array, value, side="left")
    if (idx > 0) and (idx == len(array) 
                      or math.fabs(value - array[idx-1]) 
                      < math.fabs(value - array[idx])
     ):
        return array[idx-1]
    else:
        return array[idx]

'''
    Take a dictionary of precomputed R(c,h) values and print it
'''
def print_table(r_dict, limit=None):
    for c, r_lst in r_dict.items():
        print(c, end="")
        for r in r_lst:
            print(f" {r}", end=""),
        print()
        if limit != None and c >= limit:
            break

'''
    Take precompute dictionary d using p and save it as json in dir store_dir
'''
def save_json(p, d, store_dir):
    for c, r_list in d.items():
        with open(Path(store_dir)/
                f'{p}_{c}_store.json', 'w') as fp:
            json.dump({c: r_list}, fp)

def save_json_c(p, c, r_list, store_dir):
    with open(Path(store_dir)/
            f'{p}_{c}_store.json', 'w') as fp:
        json.dump({c: r_list}, fp)

def load_json(p, c,  store_dir):
    with open(Path(store_dir)/
            f'{p}_{c}_store.json', 'r') as fp:
        d = json.load(fp)
    return d[str(c)]

def compute_Rcrt(h1, h2, r1_list, r2_list):
    inv_h1 = pow(h1, -1, h2)
    e = lambda x: ((inv_h1 * (x[1]-x[0])) % h2) * h1 + x[0]
    return [e((x0,x1)) for x0 in r1_list for x1 in r2_list]

def compute_Rx(h_list, R_list):
    assert(len(h_list) == len(R_list) and len(h_list) > 0)
    if len(h_list) == 1:
        return sorted(R_list[0])

    h1 = h_list.pop()
    h2 = h_list.pop()
    assert(isinstance(h1, int) and isinstance(h2, int))
    r1_list = R_list.pop()
    r2_list = R_list.pop()

    h_list.append(h1 * h2)
    R_list.append(compute_Rcrt(h1, h2, r1_list, r2_list))
    return h_list[0], compute_Rx(h_list, R_list)

def legendre_symbol(a, p):
    s = pow(a, (p-1)//2, p)
    return -1 if s != 1 else s

def is_QR(c, h):
    s = legendre_symbol(c, h)
    return True if s == 1 else False
