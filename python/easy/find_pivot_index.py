"""
https://leetcode.com/problems/find-pivot-index/

Runtime: 160 ms, faster than 65.67% of Python3 online submissions for Find Pivot Index.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find Pivot Index.
"""

class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        def sum_up(a: list) -> int:
            # this is an expensive calculation
            s = 0
            for i in a:
                s += i
            # print(f's {s}')
            return s

        total = sum_up(nums)
        left = 0
        for j in range(len(nums)):
            if left == (total - left - nums[j]):
                return j
            left += nums[j]
        return -1


sol = Solution()
ret = sol.pivotIndex([1, 7, 3, 6, 5, 6])
print(f'ret {ret}')


