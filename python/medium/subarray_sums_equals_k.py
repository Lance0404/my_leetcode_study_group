"""
https://leetcode.com/problems/subarray-sum-equals-k/

Time Limit Exceeded
"""


class Solution:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        def sum_equal_k(a: list) -> bool:
            # this is an expensive calculation
            s = 0
            for i in a:
                s += i
            if s == k:
                return True
            return False

        cnt = 0
        window = len(nums)
        while window > 0:
            # print(f'window {window}')
            for i in range(len(nums) - window + 1):
                sub = nums[i:i+window]
                # print(f'sub {sub}')
                # print(f'check {sum_equal_k(sub)}')
                if sum_equal_k(sub):
                    cnt += 1
            window -= 1
        return cnt



sol = Solution()
ret = sol.subarraySum([1,1,1], 2)
print(f'ret {ret}')
