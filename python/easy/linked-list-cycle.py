"""
https://leetcode.com/problems/linked-list-cycle/

Runtime: 40 ms, faster than 95.66% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
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
        turtle = head.next
        hare = head.next.next

        if hare and hare.next:
            while hare and hare.next and hare != turtle:
                hare = hare.next.next
                turtle = turtle.next
            if hare == turtle:
                return True
        return False
