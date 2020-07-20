def ATM_problem(A, X):

    # A: num of people, X: time people need
    P = X
    P = sorted(P)

    prefix_time = [0]*A

    for i in range(A):
        for j in range(0, i+1):
            prefix_time[i] += P[j]

    solution = 0
    for i in range(len(prefix_time)):
        solution += prefix_time[i]

    return solution

if __name__ == "__main__":
    A = int(input())
    X = list(map(int, input().split()))
    print(ATM_problem(A, X))