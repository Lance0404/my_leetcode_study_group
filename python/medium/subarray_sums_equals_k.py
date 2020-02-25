"""
https://leetcode.com/problems/subarray-sum-equals-k/

Time Limit Exceeded
"""


class Solution:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        # def sum_equal_k(a: list) -> bool:
        #     # this is an expensive calculation
        #     s = 0
        #     for i in a:
        #         s += i
        #     if s == k:
        #         return True
        #     return False

        # plan A failed
        # cnt = 0
        # window = len(nums)
        # while window > 0:
        #     # print(f'window {window}')
        #     for i in range(len(nums) - window + 1):
        #         sub = nums[i:i+window]
        #         # print(f'sub {sub}')
        #         # print(f'check {sum_equal_k(sub)}')
        #         if sum_equal_k(sub):
        #             cnt += 1
        #     window -= 1
        # return cnt

        # plan B failed
        # cnt = 0
        # for i in range(len(nums)):  # loop through every idx as left most
        #     sum = nums[i]
        #     if sum == k:
        #         cnt += 1
        #     for j in range(len(nums)-(i+1)):  # loop through every idx that is right of the left most
        #         print(f'i {i}, j {j}')
        #         sum += nums[i+(j+1)*1]
        #         if sum == k:
        #             cnt += 1


        # plan C failed
        cnt = 0
        for i in range(len(nums)):  # loop through every idx as left most
            cur_idx = i
            sum = nums[cur_idx]
            if sum == k:
                cnt += 1

            while cur_idx < len(nums) - 1:
                print(f'cur_idx {cur_idx}')
                cur_idx += 1
                sum += nums[cur_idx]
                if sum == k:
                    cnt += 1
        return cnt

sol = Solution()
ret = sol.subarraySum([1,1,1], 2)
print(f'ret {ret}')
# ret = sol.subarraySum([1,2,3], 3)
# print(f'ret {ret}')