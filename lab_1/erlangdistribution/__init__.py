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
