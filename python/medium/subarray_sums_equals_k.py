"""
https://leetcode.com/problems/subarray-sum-equals-k/


"""


class Solution:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        def sum_up(a: list) -> int:
            # this is an expensive calculation
            s = 0
            for i in a:
                s += i
            # print(f's {s}')
            return s

        cnt = 0

        s_len = len(nums)

        # loop through all lengths from longest to smallest
        while s_len > 0:

            s_len -= 1




sol = Solution()
ret = sol.subarraySum([1,1,1], 2)
print(f'ret {ret}')
