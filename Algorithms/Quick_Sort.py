def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    l = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    
    return quick_sort(l) + mid + quick_sort(r)