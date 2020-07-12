def merge(left, right):

    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:

            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1: ]

            else:
                result.append(right[0])
                right = right[1: ]

        elif len(left) > 0:
            result.append(left[0])
            left = left[1: ]

        elif len(right) > 0:
            result.append(right[0])
            right = right[1: ]

    return result

def merge_sort(A):

    if len(A) <= 1:
        return A

    else:
        mid = len(A) // 2
        left  = merge_sort(A[ :mid])
        right = merge_sort(A[mid: ])

        return merge(left, right)



if __name__ == "__main__":

    A = [6, 5, 3, 1, 8, 7, 2, 4]
    print(merge_sort(A))