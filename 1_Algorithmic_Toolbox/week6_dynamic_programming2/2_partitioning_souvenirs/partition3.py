# Uses python3
import sys

def partition(a, p, r):
    pivot = p
    for i in range(p + 1, r + 1):
        if(a[i] < a[pivot]):
            tmp = a[i]
            a[i] = a[pivot + 1]
            a[pivot] = tmp
            pivot = pivot + 1
    return pivot

def quickSort(a, p, r):
    if(r > p):
        x = partition(a, p, r)
        quickSort(a, p, x - 1)
        quickSort(a, x + 1, r)

def partition3(A):
    if(sum(A) % 3 == 0):
        quickSort(A, 0, len(A) - 1)
        s = [list(), list(), list()]
        i = len(A) - 1
        while(i > -1):
            j = 0
            state = False
            while(not state and j < len(s)):
                if(sum(s[j]) + A[i] <= sum(A) // 3):
                    s[j].append(A[i])
                    state = True
                j = j + 1
            i = i - 1
        return int(sum(s[0]) == sum(s[1]) == sum(s[2]) == sum(A) // 3)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

