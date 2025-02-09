# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position

''' 

approach: 
- use binary search to divide the array in half until element is found
- if element is not found, return start
- time complexity: O(log(n))
- space complexity: O(1) 

'''

class Solution:
    def searchInsert(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return start
