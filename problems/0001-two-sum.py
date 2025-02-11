# 1. Two Sum
# https://leetcode.com/problems/two-sum

''' 

approach: 
- subtract each value from target. store every num and index in hashmap. if diff exists in hashmap, return
- time complexity: O(n)
- space complexity: O(n)

'''

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i, v in enumerate(nums):
            diff = target - v

            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[v] = i

