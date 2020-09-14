def binary_search(A, left, right, k):
    # A is list to input
    # left is the most left index
    # right is the most right index
    # k is the number we try to find

    # it cannot be reversed
    if left > right:
        return None

    # mid is the middle index
    mid = (left + right) // 2

    # if the middle one is what we try to find, return it (base case)
    if k == A[mid]:
        return mid

    # recursive case
    else:
        # find the left half
        if k < mid:
            return binary_search(A, left, mid-1, k)
        # find the right half
        else:
            return binary_search(A, mid+1, right, k)

if __name__ == "__main__":

    A = [1, 2, 3, 0, 5, 6, 8, 9, 4, 7]
    # binary search works iff list to input is sorted
    A = sorted(A)

    print(binary_search(A, 0, len(A), 3))
    print(binary_search(A, 0, len(A), -1))
