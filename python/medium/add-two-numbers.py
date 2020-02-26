"""
https://leetcode.com/problems/add-two-numbers/

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Runtime: 72 ms, faster than 52.43% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # calculate the digit from the rightmost one by one
        carry = 0
        p = head = ListNode(0)
        cur_l1 = l1
        cur_l2 = l2
        while cur_l1 or cur_l2 or carry:
            l1_val = cur_l1.val if cur_l1 else 0
            l2_val = cur_l2.val if cur_l2 else 0
            val = carry + l1_val + l2_val
            carry = val // 10
            cur_l1 = cur_l1.next if cur_l1 else None
            cur_l2 = cur_l2.next if cur_l2 else None
            p.next = ListNode(val % 10)
            p = p.next
        return head.next
