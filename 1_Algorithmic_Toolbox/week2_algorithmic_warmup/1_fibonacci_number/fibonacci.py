# Uses python3
import sys


memoize = {
        0 : 0,
        1 : 1,
        }

def calc_fib_naive(n):
    if n <= 1:
        return n
    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)


def calc_fib_memoize(n):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = calc_fib_memoize(n - 1) + calc_fib_memoize(n - 2)
    return calc_fib_memoize(n - 1) + calc_fib_memoize(n - 2)


def calc_fib_iterative(n):
    previous = 0
    current = 1

    for i in range(n):
        previous, current = current, previous + current

    return previous


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(calc_fib_iterative(n))
