def binary_search_recursive(A, x):
    if len(A) == 0:
        return -1
    left, right = 0, len(A)
    mid = int((left + right) / 2)
    if x == A[mid]:
        return mid
    elif x > A[mid]:
        return binary_search(A[mid + 1:right], x)
    else:
        return binary_search(A[left:mid - 1], x)


def binary_search(A, x, left, right):
    if left >= right:
        return -1
    mid = int((left + right) / 2)
    if x == A[mid]:
        return mid
    elif x > A[mid]:
        return binary_search(A, x, mid + 1, right)
    else:
        return binary_search(A, x, left, mid - 1)


ans = binary_search(A, x, 0, len(A))


def binary_search_iterative(A, x):  # A = [3], x =5, left=0, right=1, mid=0,  x> A[mid]
    if not A:
        return -1
    left, right = 0, len(A)
    while left < right:
        mid = int((left + right) / 2)
        if x == A[mid]:
            return mid
        elif x > A[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
