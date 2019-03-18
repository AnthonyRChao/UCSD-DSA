# Uses python3
def edit_distance(s, t):
    a = len(s)
    b = len(t)

    # Handle any empty strings
    if a * b == 0:
        return a + b

    # Initalize the DP Matrix 
    D = []
    for _ in range(a + 1):
        D.append([0] * (b + 1))

    # Populate null string row and column of DP Matrix
    for i in range(a + 1):
        D[i][0] = i
    for j in range(b + 1):
        D[0][j] = j

    # Fill in DP Matrix
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            up = D[i - 1][j] + 1
            left = D[i][j - 1] + 1
            diagonal = D[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                diagonal -= 1
            D[i][j] = min(up, left, diagonal)

    return D[a][b]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
