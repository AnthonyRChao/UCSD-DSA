# Uses python3
import sys

def binary_search(a, low, high, x):
    if high < low:
        return -1
    mid = low + (high - low) // 2
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a, low, mid - 1, x)
    elif x > a[mid]:
        return binary_search(a, mid + 1, high, x)
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    low = 0
    high = len(a) - 1
    for x in data[n + 2:]:
        print(binary_search(a, low, high, x), end = ' ')
