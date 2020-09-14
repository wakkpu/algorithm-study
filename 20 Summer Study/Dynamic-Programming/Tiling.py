import sys
sys.setrecursionlimit(10**6)
global T


def Tile(n):
    if n <= 2:
        return n

    if T[n-1]:
        return T[n-1]

    T[n-1] = Tile(n-1) + Tile(n-2)
    return T[n-1]


if __name__ == "__main__":

    N = int(input())
    T = [0] * N

    print(Tile(N) % 10007)
