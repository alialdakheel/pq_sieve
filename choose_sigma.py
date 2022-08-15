import math
from tabulate import tabulate

limit = 40
e = list(range(2, limit + 1))

bound_base = math.e
# bound_base = 3

# n = [(x-1)**2 * (bound_base**(2 * x * math.log(x))) for x in e]
n = [(x-1)**2 * (x**(2 * x)) for x in e]
int_n = list(map(int, n))

bit_length = [x.bit_length() for x in int_n]
digit_length = [len(str(x)) for x in int_n]

res_dict = {
    "e": e[:10],
    # "n": int_n[:10],
    "n digits": digit_length[:10],
    "n bits": bit_length[:10],
    "e2": e[10:20],
    # "n2": int_n[10:20],
    "n digits2": digit_length[10:20],
    "n bits2": bit_length[10:20],
}

print(f"Table for choosing e (with bound base: {bound_base})")
print(tabulate(res_dict, headers='keys'))

