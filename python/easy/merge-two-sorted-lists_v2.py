"""
https://leetcode.com/problems/merge-two-sorted-lists/

Runtime: 40 ms, faster than 25.28% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add(self, head: ListNode, val: int):

        if head.next and head.val <= val <= head.next.val:
            tmp = head.next
            head.next = ListNode(val)
            head.next.next = tmp
        elif not head.next:
            head.next = ListNode(val)
        else:  # head.next.val < val
            self.add(head.next, val)  # not returning here

        return head

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            head = l1
            sub = l2
        else:
            head = l2
            sub = l1

        # cur = sub
        while sub.next:
            self.add(head, sub.val)
            sub = sub.next
        self.add(head, sub.val)

        return head
