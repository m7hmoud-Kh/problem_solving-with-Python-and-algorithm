def binary_search(elements, item):
    low = 0
    high = len(elements) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = elements[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1

    return None


elements = [1, 2, 4, 5, 6, 8, 9]

print(binary_search(elements=elements, item=2))  # print index 1
print(binary_search(elements=elements, item=10))  ## print none
