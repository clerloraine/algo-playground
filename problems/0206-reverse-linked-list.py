# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list

''' 

approach: 
- iteratively switch the pointers of each node until the head node points to null
- time complexity: O(n)
- space complexity: O(1)

'''

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev