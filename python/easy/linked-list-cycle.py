"""
https://leetcode.com/problems/linked-list-cycle/

Runtime: 48 ms, faster than 64.49% of Python3 online submissions for Linked List Cycle.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head or not head.next:
            return False
        turtle = head
        hare = head.next

        while hare != turtle:
            if not hare or not hare.next:
                return False
            hare = hare.next.next
            turtle = turtle.next
        return True
