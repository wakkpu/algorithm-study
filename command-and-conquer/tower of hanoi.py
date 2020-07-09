# https://www.acmicpc.net/problem/11729

def Hanoi(N, start, dst, temp):

    if N == 1:
        print(start, dst)

    else:
        Hanoi(N-1, start, temp, dst)
        print(start, dst)
        Hanoi(N-1, temp, dst, start)


if __name__ == "__main__":

    N = int(input())
    K = 2**N - 1
    print(K)
    Hanoi(N, start=1, dst=3, temp=2)