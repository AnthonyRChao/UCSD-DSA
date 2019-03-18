# Uses python3
import sys


def DPChange(money, coins):
    MinNumCoins = {}
    MinNumCoins[0] = 0
    for m in range(1, money + 1):
        MinNumCoins[m] = sys.maxsize
        for coin in coins:
            if m >= coin:
                NumCoins = MinNumCoins[m - coin] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(DPChange(m, [1, 3, 4]))

