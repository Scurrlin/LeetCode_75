import heapq

def top_k_elements(nums, k):
    min_heap = []
    for i in range(k):
        heapq.heappush(min_heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])
    return min_heap