def quick_sort_not_in_place(A):

    if len(A) <= 1:
        return A

    pivot = A[0] # choose pivot as the first element

    '''  
    pythonic! 
    low  = [i for i in A if i > pivot]
    mid  = [i for i in A if i == pivot]
    high = [i for i in A if i < pivot]
    '''

    low, mid, high = [], [], []

    for num in A:
        if num < pivot:
            low.append(num)

        elif num == pivot:
            mid.append(num)

        else:
            high.append(num)

    return quick_sort_not_in_place(low) + mid + quick_sort_not_in_place(high)

'''
first: the first index
last: the last index
left: index moves to right, start from the second index
right: index move to left, start from the last index
'''
def quick_sort_in_place(A, first, last):

    if first >= last:
        return None

    left, right = first+1, last

    pivot = A[first]

    while left <= right: # until they are crossed
        while left <= right and A[left] < pivot: # to find element which is larger than pivot, but on the left side
            left += 1

        while right > first and A[right] >= pivot: # to find element which is smaller than pivot, but on the right side
            right -= 1

        if left <= right: # if they are crossed, switch them and keep going
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

    A[first], A[right] = A[right], A[first]
    quick_sort_in_place(A, first, right-1) # do the same thing on the left side
    quick_sort_in_place(A, right+1, last) # do the same thing on the right side

    return A

if __name__ == "__main__":

    A = [4, 2, 6, 8, 1, 7, 3, 5]

    print(quick_sort_not_in_place(A))
    print(quick_sort_in_place(A, 0, len(A)-1))