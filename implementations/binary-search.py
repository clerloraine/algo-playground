""" 

binary search is a divide-and-conquer algo that repeatedly divides a list in half until item is found
time complexity: O(log n)
space complexity: O(1) 

"""

def binary_search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if (nums[mid] == target):
            return mid
        elif (nums[mid] > target):
            end = mid - 1
        else:
            start = mid + 1

    return -1
