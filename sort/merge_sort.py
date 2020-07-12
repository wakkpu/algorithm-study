def merge(low, high):

    result = []

    while len(low) > 0 or len(high) > 0:
        if len(low) > 0 and len(high) > 0:

            if low[0] <= high[0]:
                result.append(low[0])
                low = low[1: ]

            else:
                result.append(high[0])
                high = high[1: ]

        elif len(low) > 0:
            result.append(low[0])
            low = low[1: ]

        elif len(high) > 0:
            result.append(high[0])
            high = high[1: ]

    return result

def merge_sort(A):

    if len(A) <= 1:
        return A

    else:
        mid = len(A) // 2
        low  = merge_sort(A[ :mid])
        high = merge_sort(A[mid: ])

        return merge(low, high)



if __name__ == "__main__":

    A = [6, 5, 3, 1, 8, 7, 2, 4]
    print(merge_sort(A))