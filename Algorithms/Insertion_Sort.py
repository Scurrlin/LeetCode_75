def insertion_sort(arr):
    for idx in range(1, len(arr)):
        key = arr[idx]
        j = idx - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr