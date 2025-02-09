# 2540. Minimum Common Value
# https://leetcode.com/problems/minimum-common-value

''' 

approach: 
- for every element in the first array, do a binary search through second array
- time complexity: O(n*log m)
- space complexity: O(1)

'''

class Solution(object):
    def getCommon(self, nums1, nums2):
        for target in nums1:
            start = 0
            end = len(nums2) - 1

            while start <= end:
                mid = (start + end) // 2

                if (nums2[mid] == target):
                    return target
                elif (nums2[mid] > target):
                    end = mid - 1
                else:
                    start = mid + 1

        return -1
  
        