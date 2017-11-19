def k_nearest(arr, k, target):
    """ Given a sorted arr, return the k nearest elements to the target"""
    # O(n)
    start = 0
    for i in range(k, len(arr)):
        if abs(arr[i] - target) < abs(arr[start]-target):
            start += 1
        else:
            break
    return arr[start: start + k]




if __name__ == "__main__":
    arr = [1,4,5,7,9,10,11,12,13,14]
    print k_nearest(arr, 6, 11)
