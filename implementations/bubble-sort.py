""" 

bubble sort moves the largest unsorted element to the end of the list in each pass
time complexity: O(n^2)
space complexity: O(1) 

"""

def sort(nums):
    # outer loop - determines number of passes through the list
    for i in range(len(nums) - 1, 0, -1):
        # inner loop - swaps adjacent elements in current pass
        for j in range(i):
            if (nums[j] > nums[j+1]):
                nums[j] , nums[j+1] = nums[j+1], nums[j]