"""
https://leetcode.com/problems/happy-number/

Runtime: 32 ms, faster than 67.07% of Python3 online submissions for Happy Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Happy Number.

"""


class Solution:
    def isHappy(self, n: int) -> bool:

        # to rest with 1, we must have only one 1 digit and the other as 0 in the number
        # it should stop if the the number was encountered before
        cur = n
        store = set()
        while cur != 1:
            head = cur
            store.add(head)
            sq_sum = 0
            while cur:
                # get the right most digit
                sq_sum += (cur % 10) ** 2
                # print(f'digit {cur % 10} sq_sum {sq_sum}')
                cur //= 10
            # print(f'head {head} sq_sum {sq_sum}')

            if sq_sum in store:
                return False
            cur = sq_sum
        return True

s = Solution()
ret = s.isHappy(19)
print(f'ret {ret}')
# ret = s.isHappy(46)
# print(f'ret {ret}')
