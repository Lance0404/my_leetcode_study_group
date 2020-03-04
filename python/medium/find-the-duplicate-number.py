"""
https://leetcode.com/problems/find-the-duplicate-number/

consider the input list as a linked list
with the given assumption there must be a cycle in the linked list

use the value as a pointer
user the index as a node value

Runtime: 64 ms, faster than 83.10% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 15.2 MB, less than 17.86% of Python3 online submissions for Find the Duplicate Number.

"""

class Solution:
    def findDuplicate(self, nums: 'List[int]') -> int:

        # find the intersection of the two runners
        turtle = hare = nums[0]
        # start traversing
        turtle = nums[turtle]
        hare = nums[nums[hare]]
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[nums[hare]]

        # find the entrance to the cycle
        ptr1 = hare  # pointer 1, starts from the intersection of the turtle
        ptr2 = nums[0]  # pointer 2, starts from the the head

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]


        return ptr1

s = Solution()
ret = s.findDuplicate([1, 2, 2, 4, 3, 5])  # n = 5, answer = 2
print(f'ret {ret}')
ret = s.findDuplicate([1, 2, 4, 3, 5, 2])  # n = 5, answer = 2
print(f'ret {ret}')
ret = s.findDuplicate([5, 2, 4, 3, 5, 1])  # n = 5, answer = 5
print(f'ret {ret}')

