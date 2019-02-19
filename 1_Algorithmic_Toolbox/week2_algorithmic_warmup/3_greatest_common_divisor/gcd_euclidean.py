def gcd_euclid(a, b):
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


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd_euclid(a, b))
