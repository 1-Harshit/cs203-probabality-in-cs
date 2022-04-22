import matplotlib.pyplot as plt
import numpy as np


def random_sample(n, k):
    return np.random.choice(range(1, n+1), k)


def main():
    # input N and K
    N = int(input("N = "))

    # Holding results
    Nmid = []
    Nmean = []

    # Sampling
    for k in range(1, 1001):
        sample = random_sample(N, k)
        mean = np.mean(sample)
        median = np.median(sample)
        Nmean.append(int(mean*2+1))
        if (k % 2 == 1):
            Nmid.append(int(median*2+1))

    # Plotting
    plt.plot(range(1, 1001, 2), Nmid, 'r-', label='mean')
    plt.ylabel('N from Median')
    plt.xlabel('k')
    plt.show()

    plt.plot(range(1, 1001), Nmean, 'b-', label='median')
    plt.ylabel('N from Mean')
    plt.xlabel('k')
    plt.show()


if __name__ == '__main__':
    main()
