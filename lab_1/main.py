import numpy as np
import matplotlib.pyplot as plt

from cmath import exp


class ErlangDistribution:
    def factorial(self, n):
        factorial_ans = 1
        for i in range(1, n + 1):
            factorial_ans = factorial_ans * i
        return factorial_ans

    def distributionFunction(self, x, k, lambda_v):
        summ = 0

        for i in range(0, k):
            summ += 1 / self.factorial(i) * exp(-lambda_v * x) * pow((lambda_v * x), i)

        return 1 - summ

    def densityFunction(self, x, k, lambda_v):
        return pow(lambda_v, k) * pow(x, k - 1) * exp(-lambda_v * x)


def main():
    a = float(input("Enter start point a: "))
    b = float(input("Enter end point b: "))
    k = int(input("Enter k: "))
    lambda_v = float(input("Enter lambda: "))

    delta = b - a

    x_uniform = np.arange(a - delta / 2, b + delta / 2, 0.001)

    y_uniform_cdf = [uniform_distribution_cdf(a, b, value) for value in x_uniform]
    y_uniform_pdf = [uniform_distribution_pdf(a, b, value) for value in x_uniform]

    draw_plots(x_uniform, y_uniform_cdf, y_uniform_pdf, k, lambda_v)


def draw_plots(x, y_cdf, y_pdf, k, lambda_v):
    fig, axs = plt.subplots(2, figsize=(6, 7))

    axs[0].plot(x, y_cdf)
    axs[1].plot(x, y_pdf)

    axs[0].set_xlabel('$x$')
    axs[0].set_ylabel('$F(x)$')

    axs[1].set_xlabel('$x$')
    axs[1].set_ylabel('$f(x)$')

    axs[0].grid(True)
    axs[1].grid(True)

    plt.show()

    erlang_f(k, lambda_v)


def uniform_distribution_cdf(a, b, x):
    return (x - a) / (b - a) if (a <= x < b) else 0 if x < a else 1


def uniform_distribution_pdf(a, b, x):
    return 1 / (b - a) if (a <= x <= b) else 0

def erlang_f(k, lambda_v):
    fig, axs = plt.subplots(2, figsize=(6, 7))

    dist_1 = []
    dist_2 = []

    a = 0
    b = 12
    step = (b - a) / 100
    #
    # k = 8
    # lambda_v = 0.9

    steps = []

    while a < b:
        steps.append(a)
        dist_1.append(ErlangDistribution().distributionFunction(
            a, k, lambda_v
        ))
        dist_2.append(ErlangDistribution().densityFunction(
            a, k, lambda_v
        ))
        a += step

    axs[0].plot(steps, dist_1)
    axs[1].plot(steps, dist_2)

    axs[0].set_ylabel('$F(x)$')
    axs[1].set_ylabel('$p(x)$')

    axs[0].grid(True)
    axs[1].grid(True)

    plt.show()


if __name__ == '__main__':
    main()
