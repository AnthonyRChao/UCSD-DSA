# Uses python3
import sys

def get_change(m):
    choices = [10, 5, 1]
    res = 0
    for choice in choices:
        coins = m // choice
        if coins > 0:
            res = res + coins
            m = m - choice * coins
    return res

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
