def find_max1(A):

    if len(A) == 1:
        return A[0]

    else:
        return max(A[0], find_max1(A[1: ]))
def find_max2(A):

    if len(A) < 1:
        return None

    elif len(A) == 1:
        return A[0]

    else:
        return max(find_max2(A[ :len(A)//2]), find_max2(A[len(A)//2: ]))

if __name__ == "__main__":

    A = [1, 3, 5, 4, 9, 6, 7]
    print(find_max1(A))
    print(find_max2(A))
