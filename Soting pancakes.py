def pancake_sort(array):
    def flip(arr, end):
        start = 0
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(array)
    for i in range(n, 0,-1):
        # Find the index of the maximum element in the unsorted part of the list
        max_idx = array.index(max(array[:i]))

        # Flip the elements from the start of the list to the index of the maximum element
        if max_idx != 0:
            flip(array, max_idx)

        # Flip the elements from the start of the list to the end of the unsorted part of the list
        flip(array, i - 1)

    return array

array = [5, 2, 7, 3, 8, 6]
sorted_array = pancake_sort(array)
print(sorted_array)