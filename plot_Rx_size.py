
import util
import sys
from precompute import precompute_c, is_precomputed, load_primes
from pq_sieve import PQSieve

def exp_step(num_p):
    primes= load_primes("primes.txt")
    primes = primes[:num_p]
    print("primes", primes, "size", sys.getsizeof(primes))

    #Experiment RSA-110
    pqs_rsa1 = PQSieve(35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667, h=[], num_p=num_p)
    return sys.getsizeof(pqs_rsa1.R)

def exp():
    size_list = list()
    for i in range(1, 11):
        print(f"======== Exp: (num_p: {i}) ========")
        Rx_size = exp_step(i)
        size_list.append(Rx_size)
    return size_list

def plot(size_list):
    #import matplotlib
    import matplotlib.pyplot as plt
    #matplotlib.use('TKAgg')
    fig, ax = plt.subplots()
    ax.plot(list(range(1,len(size_list)+1)), size_list, 'o--')
    plt.show()

if __name__=="__main__":
    s_list = exp()
    plot(s_list)
