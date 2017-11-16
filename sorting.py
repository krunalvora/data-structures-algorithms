# Divide and Conquer Algorithm
def merge_sort_recursive(arr):
    # O(nlogn) time complexity

    # Base Case:
    if len(arr) == 1:
        return arr

    # Resursively solve part of the problem
    mid = len(arr) / 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    # Do the remaining part of the problem
    i = j = k = 0
    # merge the left and right arr in a sorted manner till both last
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # add the remainder of the left array if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    # add the remainder of the right array if any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    # Attaching these parts is not required in this case as the original arr is merged completely from the left and right arrays
    # Returning
    return arr



def bubble_sort_iterative(arr):
    # Outer loop that goes backwards
    # The last element of the outer loop gets into its position at every iteration
    for outer in reversed(range(len(arr))):
        # Inner loop traverses through the outer loop range
        # Adjacent comparisons push the highest element to the right LIKE A BUBBLE sideways
        for inner in range(outer):
            if arr[inner] > arr[inner + 1]:
                arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]
    return arr

def bubble_sort_recursive(arr, upto): # upto but not including
    # Base case
    if upto < 1:
        return arr
    # Do part of the problem
    for i in range(upto - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # Recursively solve the remaining part of the solution
    bubble_sort_recursive(arr, upto - 1)
    # Attaching not needed here as the arr is being returned completely
    # Returning
    return arr


def insertion_sort_iterative(arr):
    for to_be_inserted in range(1, len(arr)):
        for temp in range(to_be_inserted, 0, -1):
            if arr[temp] < arr[temp - 1]:
                arr[temp], arr[temp - 1] = arr[temp - 1], arr[temp]
            else:
                break
    return arr

def insertion_sort_recursive(arr, length):
    if length == 1:
        return arr
    insertion_sort_recursive(arr, length - 1)
    to_be_inserted = length - 1
    for temp in range(to_be_inserted, 0, -1):
        if arr[temp] < arr[temp - 1]:
            arr[temp], arr[temp - 1] = arr[temp - 1], arr[temp]
        else:
            break
    return arr



if __name__ == "__main__":
    arr = [2,3,6,9,4,1,52]
    #print insertion_sort_iterative(arr)
    print insertion_sort_recursive(arr, len(arr))
