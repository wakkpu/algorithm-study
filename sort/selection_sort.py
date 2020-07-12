def selection_sort(A):

    for i in range(len(A)-1):
        min_index = i

        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]

    return A

if __name__ == "__main__":

    A = [3, 4, 5, 5, 1, 2]
    print(selection_sort(A))