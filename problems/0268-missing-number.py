# 268. Missing Number
# https://leetcode.com/problems/missing-number

''' 

approach 1: 
- sort the list
- iterate through all possible numbers and perform binary search 
- if number is not found, return number
- time complexity: O(n log n)
- space complexity: O(1) 

'''

class SolutionBinarySearch(object):
    def missingNumber(self, nums):
        nums.sort()  
        
        for i in range(len(nums) + 1):  
            start, end = 0, len(nums) - 1
            
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == i:
                    break
                elif nums[mid] > i:
                    end = mid - 1
                else:
                    start = mid + 1
            
            if start > end:
                return i
            
              
''' 

approach 2: 
- sum formula
- calculate the expected sum of numbers till n, and subtract with the actual sum
- time complexity: O(n)
- space complexity: O(1) 

'''


class SolutionSumFormula(object):
    def missingNumber(self, nums):
        n = len(nums)
        actual_sum = sum(nums)
        expected_sum = sum(range(n + 1))

        return expected_sum - actual_sum