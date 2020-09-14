def bubble_sort(A):

    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]

    return A

def bubble_sort_optimized_1(A):

    for i in range(len(A)):
        swapped = False

        for j in range(len(A)-1, i, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                swapped = True

        if not swapped:
            break

    return A

def bubble_sort_optimized_2(A):

    end = len(A)-1

    while end > 0:
        last_swap = 0

        for i in range(end):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                last_swap = i

        end = last_swap

    return A

if __name__ == "__main__":

    A = [3, 8, 2, 1, 4, 5, 7, 6]

    print(bubble_sort(A))
    print(bubble_sort_optimized_1(A))
    print(bubble_sort_optimized_2(A))