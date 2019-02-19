def gcd(a, b):
    best = 1
    for num in range(2, min(a, b) + 1):
        if a % num == 0 and b % num == 0:
            if num > best:
                best = num
    return best


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))
