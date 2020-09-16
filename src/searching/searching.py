# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        # Base case for target not found
        return -1
    else:
        # Split the array into 2
        mid = (start + end) // 2
        # Base case to check if target number is our midpoint
        if target is arr[mid]:
            return mid
        elif target < arr[mid]:
            # Run function on left side of the tree
            return binary_search(arr, target, start, mid - 1)
        else:
            # Run function on right side of the tree
            return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
