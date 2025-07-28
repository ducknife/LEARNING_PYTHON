
def binary_search(array, left, right, target):
    if right < left:
        return -1
    else:
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return -1

