"""
https://leetcode.com/problems/happy-number/

Runtime: 32 ms, faster than 67.07% of Python3 online submissions for Happy Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Happy Number.

two pointer solution
"""


# so we can probably use cycle detection to solve this
# if it will encounter a same number then there must be a cycle

class Solution:

    def isHappy(self, n: int) -> bool:

        def transform(cur):
            sq_sum = 0
            while cur:
                sq_sum += (cur % 10) ** 2
                cur //= 10
            return sq_sum  # a copy operation

        def is_one(a: int) -> bool:
            # print(f'is_one({a})')
            while a // 10 > 0:
                if a % 10 != 0:
                    return False
                a //= 10
            # now we get the left most a
            if a == 1:
                return True
            return False

        # if there is a cycle then it's not a happy number

        if not is_one(n):
            fast = transform(transform(n))
            slow = transform(n)
            while not is_one(fast) and not is_one(slow) and fast != slow:
                fast = transform(transform(fast))  # trans twice
                slow = transform(slow)  # trans once
                # print(f'{slow} {fast}')

            if is_one(fast) or is_one(slow):
                # print(f'Lance debug: {slow} {fast}')
                return True
            return False
        return True


s = Solution()
ret = s.isHappy(13)
print(f'ret {ret}')

