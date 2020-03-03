"""
https://leetcode.com/problems/linked-list-cycle-ii/

Runtime: 48 ms, faster than 75.48% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.

please check others' solution
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        first = head.next
        second = head.next.next

        while second and second.next and first != second:
            first = first.next
            second = second.next.next

        if not second or not second.next:
            return None

        second = head
        while first and second and first != second:
            first = first.next
            second = second.next
        if first == second:
            return second

        return None
