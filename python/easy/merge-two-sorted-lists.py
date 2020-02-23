"""
https://leetcode.com/problems/merge-two-sorted-lists/

It turns out that class ListNode is not meant to be modified.

But I wanna keep this.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, a: int, head: 'ListNode' = None):
        print(f'add({a})')
        # if not head:
        #     head = self

        if not self.next:
            self.next = ListNode(a)
        else:
            self.next.add(a)

    def insert(self, b: int):
        if self.val <= b and not self.next:
            self.next = ListNode(b)
        elif self.val <= b <= self.next.val:
            tmp = self.next
            self.next = ListNode(b)
            self.next.next = tmp
        else:
            self.next.insert(b)

    def to_list(self) -> list:
        ret = []
        cur = self
        while cur.next:
            ret.append(cur.val)
            cur = cur.next
        ret.append(cur.val)
        return ret

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # set the current ListNode with the one having the smallest head
        ln1 = l1
        ln2 = l2
        if ln1.val <= ln2.val:
            main = ln1
            sub = ln2
        else:
            main = ln2
            sub = ln1
        print(f'main {main.to_list()}')
        print(f'sub {sub.to_list()}')

        # add the "sub" in to the "main"
        while sub.next:
            main.insert(sub.val)
            sub = sub.next
        main.insert(sub.val)
        print(f'main {main.to_list()}')
        return main

ln1 = ListNode(1)
ln1.add(2)
ln1.add(4)
#
# print(f'ln1 {ln1.to_list()}')

# print(ln1.val)
# print(ln1.next.val)
# print(ln1.next.next.val)
#
ln2 = ListNode(1)
ln2.add(3)
ln2.add(4)
#
s = Solution()
ret = s.mergeTwoLists(ln1, ln2)
print(f'ret {ret}') # [1,1,2,3,4,4]

# s = Solution()
# ret = s.mergeTwoLists([1,2,4], [1,3,4,5])
# print(f'ret {ret}') # [1,1,2,3,4,4]