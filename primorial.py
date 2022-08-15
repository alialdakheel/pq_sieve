import math
from operator import mul
from functools import reduce
from precompute import load_primes
from tabulate import tabulate

limit = 20
m = list(range(1, limit + 1))
primes = load_primes("primes.txt", limit=limit) 

primorial = [reduce(mul, primes[:l]) for l in range(1,limit + 1)]
adj_primes = [primes[0]**6, primes[1]**2, primes[2]**2] + primes[3:]
x = [reduce(mul, adj_primes[:l]) for l in range(1,limit + 1)]

bound_b2 = [2**(x*math.log2(x)) for x in m]
bound_be = [math.e**(x*math.log2(x)) for x in m]
bound_b3 = [3**(x*math.log2(x)) for x in m]

res_dict = {
    "primorial" : map(float, primorial),
    "x" : map(float, x),
    "bound_b2" : bound_b2,
    "bound_be" : bound_be,
    "bound_b3" : bound_b3,
}
print(tabulate(res_dict, headers='keys'))
