def two_sum(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        curr_sum = arr[l] + arr[r]
        if curr_sum == target:
            return [l, r]
        elif curr_sum < target:
            l += 1
        else:
            r -= 1
    return []