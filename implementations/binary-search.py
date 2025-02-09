""" 

binary search is a divide-and-conquer algo that repeatedly divides a list in half until item is found
time complexity: O(log n)
space complexity: O(1) 

"""

def binary_search(nums, target):
    def search(start, end):
        if start > end:  
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            return search(start, mid - 1) 

        else:
            return search(mid + 1, end)  

    return search(0, len(nums) - 1)
