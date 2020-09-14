def activity_selection(S, F):

    L = [0]
    k = 0

    for i in range(1, len(S)):
        if S[i] >= F[k]:
            L.append(i)
            k = i

    return L


if __name__ == "__main__":

    S = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    F = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    print(activity_selection(S, F))