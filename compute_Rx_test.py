
from compute_Rx import RX
import gc
import numpy as np

examples = [
             12759908025574684369,
             12759908025574684369,
             223710178181483884087,
             223710178181483884087,
             # 223710178181483884087,
             # 223710178181483884087,
             # 4014363189286667855933,
             # 52273100668689816612043,
             # 1000424515683925933626023,
             # 13264984799917245005244533,
             # 3677169269011909330112649617,
             # 62821100886317431913009499013,
             # 1026521762973406557162751475101,
             ]

num_p_list = [
               7,
               8,
               6,
               7,
               8,
               9,
               # 10,
               # 9,
               # 11,
               # 9,
               # 8,
               # 10,
               # 10,
            ]

def test_np():
    for n, num_p in zip(examples, num_p_list):
        print(f"Testing {n} with {num_p} primes")

        rx = RX(n, num_p=num_p)
        print("Truth Primes:", rx.primes_used)
        true_x, truth = rx._compute_Rx()
        del rx
        gc.collect()

        rx = RX(n, num_p=num_p)
        print("Primes:", rx.primes_used)
        x, Rx = rx._compute_Rx_np(dtype=object)

        # Rx = sorted(Rx.tolist())
        Rx = np.sort(Rx).tolist()
        truth = sorted(truth)
        if len(Rx) == len(truth) and x == true_x:
            passed = True
            for i in range(len(truth)):
                check = (Rx[i] == truth[i])
                if not check and Rx[i] not in truth:
                    print(f"Check {check} for truth: {truth[i]},"
                          f"while Rx: {Rx[i]} at index: {i}")
                passed = passed and check
            print(f"{n} with {num_p} primes: Passed {passed}")
        else:
            print(f"{n} with {num_p} primes: Failed")
        del rx
        del truth
        del Rx
        gc.collect()

def plot_time(param_list, time_list):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(self.bit_lengths, self.search_times, 'o--',
            self.bit_lengths, self.qs_times, 'o--')
    fig.savefig('compute_one_time_graph.png')

def test_compute_one_time():
    print(f"Testing {n} with {num_p} primes")

    rx = RX(n, num_p=num_p)
    print("Truth Primes:", rx.primes_used)
    true_x, truth = rx._compute_Rx()

def test_gen(lim):
    for n, num_p in zip(examples, num_p_list):
        print(f"Testing {n} with {num_p} primes")

        rx = RX(n, num_p=num_p)
        print("Truth Primes:", rx.primes_used)
        rx_gen = rx.Rx_gen()
        R = [next(rx_gen) for _ in range(lim)]
        print("Rx:", R)


if __name__=="__main__":
    lim = 30
    test_gen(lim)
