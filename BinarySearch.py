def binarySearch(start, end, nums, target):
    while (start <= end):
        mid = start + (end - start) // 2 #Treat mid as offset from start, not absolute index.
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

def searchLeftBoundary(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    Time O(log N)
    Space: O(1)

    In ascending array, find the position of the last element that's < target OR first element that's = target.
    This is the LEFT boundary
    
    eg: 
    [1,3,3,3,5,7], target = 4 will return 3 (4th element)
    [1,3,3,3,5,7], target = 3 will return 1 (2nd element)
    [3], target = 3 will return 0 (1st element)
    [2], target = 3 will return 0 (1st element)
    [4], target = 3 will return -1 (an out of bound element, as such a boundary does not exist)
    """
    start, end = 0, len(nums)-1
    index = None
    while start <= end:
        mid = start + (end - start) // 2
        if target <= nums[mid]:
            end = mid -1
        elif target > nums[mid]:
            start = mid + 1
        if target >= nums[mid]:
            index = mid
    if index is not None:
        return index
    else:
        return end


def searchRightBoundary(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    Time O(log N)
    Space: O(1)

    In ascending array, find the position of the first element that's > target OR last element that's = target.
    This is the RIGHT boundary.
    
    eg: 
    [1,3,3,3,5,7], target = 4 will return 4 (5th element)
    [1,3,3,3,5,7], target = 3 will return 3 (4th element)
    [3], target = 3 will return 0 (1st element)
    [2], target = 3 will return 1 (an out of bound element, as such a boundary does not exist)
    [4], target = 3 will return 0 (1st element)    
    """
    start, end = 0, len(nums)-1
    index = None
    while start <= end:
        mid = start + (end - start) // 2
        if target >= nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        if target == nums[mid]:
            index = mid
    if index is not None:
        return index
    else:
        return start
