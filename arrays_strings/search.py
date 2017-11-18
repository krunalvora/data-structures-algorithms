def binary_search(arr, target):
    if arr[0] > target or arr[len(arr) - 1] < target:
        return -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            # Found the target
            return mid
        elif arr[mid] > target:
            # Target resides on the left hand side
            end = mid - 1
        else:
            # Target resides on the right hand side
            start = mid + 1
    return -1

if __name__ == "__main__":
    arr = [2,3,6,9,4,1,52]
    sorted_arr = [1,3,5,7,9,11,13]
    print binary_search(sorted_arr, 13)
