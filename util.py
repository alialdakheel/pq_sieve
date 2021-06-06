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
