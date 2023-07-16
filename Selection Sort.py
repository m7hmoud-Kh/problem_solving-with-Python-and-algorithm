def selection_sort(arr):
    new_arr = []

    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

def find_smallest(arr):
    smallest = arr[0]
    small_index = 0

    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            small_index = i
    return small_index

arr = [5, 8, 2, 4, 9, 20, 1]

sorted_arr = selection_sort(arr)
print(sorted_arr)