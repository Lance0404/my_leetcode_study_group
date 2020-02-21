"""
https://leetcode.com/problems/merge-two-sorted-lists/

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, a: int):
        if not self.next:
            self.next = ListNode(a)
        else:
            self.next.add(a)

    def insert(self, b: int):
        if b < self.val:
            # todo
            # ListNode()
        elif self.val < b <= self.next:
            tmp = self.next
            self.next = ListNode(b)
            self.next.next = tmp
        else:
            # todo



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # insert l2 into l1
        cur = l2
        while cur.next:
            l1.insert(cur.val)
            cur = cur.next
        return l1

ln1 = ListNode(1)
ln1.add(2)
ln1.add(4)

print(ln1.val)
print(ln1.next.val)
print(ln1.next.next.val)

ln2 = ListNode(1)
ln2.add(3)
ln2.add(4)

s = Solution()
ret = s.mergeTwoLists(ln1, ln2)
print(f'ret {ret}') # [1,1,2,3,4,4]


