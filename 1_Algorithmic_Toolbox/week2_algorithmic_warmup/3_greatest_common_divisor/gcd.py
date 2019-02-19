# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_recursive_euclid(a, b):
    """Lemma:
        Let a' be the remainder when a is divided by d, then:

            gcd(a, b) = gcd(a', b) = gcd(b, a')

            a = a' + bq for some value, q
            d divides a if and only if it divides a' and b
    """
    a_prime = a % b
    if a_prime == 0:
        return b
    return gcd_euclid(b, a_prime)


def gcd_iterative(a, b):
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_iterative(a, b))
