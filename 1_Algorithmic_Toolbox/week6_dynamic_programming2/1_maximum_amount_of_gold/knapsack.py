# Uses python3
import sys

def optimal_weight(W, w):
    res = [[0 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for weight in range(1, W + 1):
            res[i][weight] = res[i - 1][weight]
            if w[i - 1] <= weight:
                value = res[i - 1][weight - w[i - 1]] + w[i - 1]
                if value > res[i][weight]:
                    res[i][weight] = value
    return res[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
