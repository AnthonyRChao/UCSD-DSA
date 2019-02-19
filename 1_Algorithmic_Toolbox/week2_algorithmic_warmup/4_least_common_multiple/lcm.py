# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_starting_from_greater(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    for i in range(greater, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i
    return a * b


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

