# Uses python3
memoize = {
        0 : 1,
        1 : 1,
        }

def calc_fib(n):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
