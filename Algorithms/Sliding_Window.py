def max_subarr_sum(arr, k):
    if len(arr) < k:
        return -1
    max_sum = curr_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

# curr = current

def max_sliding_window(nums, k):
    from collections import deque
    deq = deque()
    result = []
    for i in range(len(nums)):
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result