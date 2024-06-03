def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    l = [x for x in arr if x < p]
    mid = [x for x in arr if x == p]
    r = [x for x in arr if x > p]
    return quick_sort(l) + mid + quick_sort(r)

# p = pivot
# l = left
# mid = middle
# r = right