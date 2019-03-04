'''
Mathematic Formulation of Fractional Knapsack Problem

W = capacity of knapsck
wi = weight of item
vi = value of item
A = list tracking weights of items added

Knapsack(W, w1, v1, ... , wn, vn)

A <- [0, 0, ... , 0], V <- 0
repeat n times:
    if W = 0:
        return (V, A)
    select i with wi > 0 and max vi/wi
    a <- min(wi, W)
    V <- V + a(vi/wi)
    wi <- wi - a, A[i] <- A[i] + a, W <- W - a
return (V, A)
'''

# Uses python3
import sys

def get_optimal_value(C, weights, values):
    V = 0.
    A = [0] * n

    # determine value weights for each item 
    vw = [v/w for (v,w) in zip(values, weights)]

    # iterate n times
    for _ in range(n):
        if C == 0:
            print('V, A:', V, A)
            return V
        # select i with wi > 0 and max vi/wi
        i = vw.index(max(vw))
        if weights[i] > 0:
            a = min(weights[i], C)
            V = V + a * vw[i]
            weights[i] = weights[i] - a
            C = C - a
            A[i] = A[i] + a
        vw.pop(i), weights.pop(i), values.pop(i)
    print('V, A:', V, A)
    return V


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, C = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(C, weights, values)
    print("{:.10f}".format(opt_value))


