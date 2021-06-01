import json
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
