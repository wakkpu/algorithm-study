def insertion_sort(A):

    for end in range(1, len(A)):
        for i in range(end, 0, -1):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]

    return A

def insertion_sort_optimized_1(A):

    for end in range(1, len(A)):
        i = end

        while i > 0 and A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
            i -= 1

    return A

def insertion_sort_optimized_2(A):

    for end in range(1, len(A)):
        value_to_insert = A[end]
        i = end

        while i > 0 and A[i-1] > value_to_insert:
            A[i] = A[i-1]
            i -= 1

        A[i] = value_to_insert

    return A

if __name__ == "__main__":

    A = [4, 2, 3, 5, 1, 6]

    print(insertion_sort(A))
    print(insertion_sort_optimized_1(A))
    print(insertion_sort_optimized_2(A))