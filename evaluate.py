'''
Author: Ali @ C4C.KACST
'''

from pq_sieve import PQSieve
from time import time
from tabulate import tabulate
import sys
sys.path.append("../quadratic_sieve/")
import factor as qs

class Eval:
    def __init__(self, methods=['p+qS', 'QS'], examples=[]):
        self.methods = methods
        if (len(examples)):
            self.examples = examples
        else:
            self.examples = [#12759908025574684369,
                             12759908025574684369,
                             12759908025574684369,
                             #223710178181483884087,
                             #223710178181483884087,
                             #223710178181483884087,
                             #223710178181483884087,
                             223710178181483884087,
                             #4014363189286667855933,
                             4014363189286667855933,
                             #52273100668689816612043,
                             52273100668689816612043,
                             #1000424515683925933626023,
                             #1000424515683925933626023,
                             #1000424515683925933626023,
                             1000424515683925933626023,
                             #13264984799917245005244533,
                             13264984799917245005244533,
                             3677169269011909330112649617,
                             #62821100886317431913009499013,
                             #62821100886317431913009499013,
                             62821100886317431913009499013,
                             #1026521762973406557162751475101,
                             1026521762973406557162751475101,
                             ]
            self.num_p_list = [
                               #6,
                               7,
                               8,
                               #6,
                               #7,
                               #8,
                               #9,
                               10,
                               #9,
                               10,
                               #8,
                               9,
                               #8,
                               #9,
                               #10,
                               11,
                               #8,
                               9,
                               8,
                               #8,
                               #9,
                               10,
                               #9,
                               10,
                               ]

        self.bit_lengths = [n.bit_length() for n in self.examples]
        self.digit_lengths = [len(str(n)) for n in self.examples]

    def evaluate(self):
        self.init_times = list()
        self.search_times = list()
        self.qs_times = list()
        self.qs_res_list = list()
        self.res_list = list()
        self.primes_used_list = list()
        for n, num_p in zip(self.examples, self.num_p_list):
            self._evaluate_one(n, num_p)

    def _evaluate_one(self, n, num_p):
            print(n, num_p)
            start_init_time = time()
            pqs = PQSieve(n, h=[], num_p=num_p,
                          progress=False
                          )
            end_init_time = time()

            start_search_time = time()
            res = pqs.search()
            end_search_time = time()

            self.init_times.append(end_init_time - start_init_time)
            self.search_times.append(end_search_time - start_search_time)
            self.res_list.append(res)
            self.primes_used_list.append(pqs.primes_used)
            del pqs

            start_qs_time = time()
            qs_res = qs.factor(n)
            end_qs_time = time()
            self.qs_times.append(end_qs_time - start_qs_time)
            self.qs_res_list.append(qs_res)

    def plot(self):
        import matplotlib.pyplot as plt
        #matplotlib.use('TKAgg')
        fig, ax = plt.subplots()
        ax.plot(self.bit_lengths, self.search_times, 'o--',
                self.bit_lengths, self.qs_times, 'o--')
        fig.savefig('evaluation_graph.png')


if __name__ == "__main__":
    ev = Eval()
    ev.evaluate()
    results = {"n": ev.examples,
               "n digits": ev.digit_lengths,
               "n bits": ev.bit_lengths,
               "num_p": ev.num_p_list,
               "primes": ev.primes_used_list,
               "pqs Rx time (s)": ev.init_times,
               "pqs search time (s)": ev.search_times,
               "qs factoring time (s)": ev.qs_times
               }

    print(tabulate(results, headers='keys'))
