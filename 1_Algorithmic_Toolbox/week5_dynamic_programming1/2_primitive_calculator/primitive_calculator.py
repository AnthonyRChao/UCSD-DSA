# Uses python3
import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)


def optimal_sequence(n):
    mNO = [0] * (n + 1)
    for num in range(2, n + 1):
        numOps = []
        if num % 3 == 0:
            numOps.append(mNO[num // 3] + 1)
        if num % 2 == 0:
            numOps.append(mNO[num // 2] + 1)
        numOps.append(mNO[num - 1] + 1)
        mNO[num] = min(numOps)

    sequence = []
    while n >= 1:
        sequence.append(n)
        toAppend = []
        if n % 3 == 0:
            toAppend.append((mNO[n // 3], n // 3))
        if n % 2 == 0:
            toAppend.append((mNO[n // 2], n //2))
        toAppend.append((mNO[n - 1], n - 1))
        n = min(toAppend)[1]

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
