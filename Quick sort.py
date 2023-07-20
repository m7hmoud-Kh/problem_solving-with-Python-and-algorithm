def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [i for i in arr if i < pivot]
    greater = [i for  i in arr if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


arr = [10,20,50,80,3,2,5,8,18]
print(quick_sort(arr))