# 4.1 Write out the code for the earlier sum function.


def sum_recursive(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_recursive(arr[1:])
arr = [1,2,7]
print(sum_recursive(arr,))


#4.2 Write a recursive function to count the number of items in a list.

def count_recursive(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_recursive(arr[1:])

arr = [1,2,7]
print(count_recursive(arr))

#Find the maximum number in a list

def max_number(arr):
    max_item = arr[0]
    for item in range(len(arr)):
        if  arr[item] > max_item:
            max_item = arr[item]
    return max_item

arr = [1,2,7,20]
print(max_number(arr))
