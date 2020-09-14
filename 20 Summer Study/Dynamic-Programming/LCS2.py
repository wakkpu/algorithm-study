def LCS2(X, Y):

    x, y = len(X), len(Y)
    table = [[0] * (y+1) for _ in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if X[i-1] == Y[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])

    return int(table[x][y])


if __name__ == "__main__":

    X = str(input())
    Y = str(input())

    print(LCS2(X, Y))