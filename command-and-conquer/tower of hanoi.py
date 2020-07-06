# https://www.acmicpc.net/problem/11729

def Hanoi(N, start, to, via):

    if N == 1:
        print(start, to)

    else:
        Hanoi(N-1, start, via, to)
        print(start, to)
        Hanoi(N-1, via, to, start)


if __name__ == "__main__":

    N = int(input())
    K = 2**N - 1
    print(K)
    Hanoi(N, start=1, to=3, via=2)