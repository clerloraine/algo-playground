""" 

selection sort repeatedly scans the unsorted portion of the list and moves the smallest to its correct position.
time complexity: O(n^2)
space complexity: O(1) 

"""

def sort(nums):
    # outer loop - controls the unsorted portion
    for i in range(len(nums) - 1):
        smallest = i

        # inner loop - finds the smallest element in the unsorted portion
        for j in range(i + 1, len(nums)):
            if (nums[j] < nums[smallest]):
                smallest = j

        nums[i], nums[smallest] = nums[smallest], nums[i]