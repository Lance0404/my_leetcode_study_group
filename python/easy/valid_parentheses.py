"""
https://leetcode.com/problems/valid-parentheses/

Runtime: 28 ms, faster than 72.25% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""


class Solution:

    def isValid(self, s: str) -> bool:

        a1 = '('
        a2 = ')'
        b1 = '['
        b2 = ']'
        c1 = '{'
        c2 = '}'

        def is_counter(left, right):
            if (left == a1 and right == a2) or (left == b1 and right == b2) or (left == c1 and right == c2):
                return True
            return

        if len(s) % 2 != 0:
            return False
        head = []
        for i in s:
            # print(f'i {i}')
            if i in [a1, b1, c1]:
                head.append(i)
            elif i in [a2, b2, c2]:
                if len(head) == 0 or not is_counter(head.pop(), i):
                    return False
        if len(head) > 0:
            return False
        return True


s = Solution()
ret = s.isValid('{[}]')
print(f'ret {ret}')
ret = s.isValid('{}')
print(f'ret {ret}')
ret = s.isValid('{[]}')
print(f'ret {ret}')
ret = s.isValid('{')
print(f'ret {ret}')
ret = s.isValid('((')
print(f'ret {ret}')
ret = s.isValid('][')
print(f'ret {ret}')
