import sys
sys.setrecursionlimit(10**6)

N = int(input())
T = [0] * N


def Tile(n):
    if n <= 2:
        return n

    if T[n-1]:
        return T[n-1]

    T[n-1] = Tile(n-1) + Tile(n-2)
    return T[n-1]


print(Tile(N) % 10007)
