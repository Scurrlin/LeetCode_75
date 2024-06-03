def binary_search(arr, t):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# t = target
# l = left
# r = right