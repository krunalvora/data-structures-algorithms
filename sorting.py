# Divide and Conquer Algorithm
def merge_sort(arr):
    # O(nlogn) time complexity

    # Base Case:
    if len(arr) == 1:
        return arr

    # Split recursively
    mid = len(arr) / 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    # Merging two sorted lists
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
    return arr










def quick_sort(arr):
    



if __name__ == "__main__":
    arr = [2,3,6,9,4,1,52]
    print merge_sort(arr)
