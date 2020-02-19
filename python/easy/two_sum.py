"""
https://leetcode.com/problems/two-sum/

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Runtime: 2804 ms, faster than 20.89% of Python3 online submissions for Two Sum.
Memory Usage: 13.7 MB, less than 77.67% of Python3 online submissions for Two Sum.

"""

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        print(f'len nums {len(nums)}')
        for i in range(len(nums)):
            # print(f'i {i}')
            for j in range(i):
                # print(f'i {i} j {j}')
                if nums[i] + nums[j] == target:
                    # print('return here')
                    return [j, i]


s = Solution()
nums = [2,7,11,15]
target = 26
ret = s.twoSum(nums, target)
print(f'ret {ret}')

