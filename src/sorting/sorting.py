# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0
    # loop through new array
    for i in range(len(merged_arr)):
        # if index at b is out of range, insert from a
        if a > len(arrA) - 1:
            merged_arr[i] = arrB[b]
            # increment ib
            b += 1
        # flipped case for above
        elif b > len(arrB) - 1:
            merged_arr[i] = arrA[a]
            # increment ia
            a += 1
        # if current index in a is smaller than b, then insert from list a
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # flipped case for above
        elif arrB[b] < arrA[a]:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # Base case for recursion
    if len(arr) <= 1:
        return arr
    else:
        # split the array in half
        mid = len(arr) // 2
        # sort left side of array
        left = merge_sort(arr[:mid])
        # sort right of array
        right = merge_sort(arr[mid:])
        # merge arrays back together with helper function from above
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here
