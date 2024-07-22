def two_sum(arr, t):
    l, r = 0, len(arr) - 1
    while l < r:
        curr_sum = arr[l] + arr[r]
        if curr_sum == t:
            return [l, r]
        elif curr_sum < t:
            l += 1
        else:
            r -= 1
    return []

# t = target
# l = left
# r = right
# curr = current