"""
https://leetcode.com/problems/remove-element/

Runtime: 32 ms, faster than 57.95% of Python3 online submissions for Remove Element.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Element.

"""


class Solution:
    def removeElement(self, nums: 'List[int]', val: int) -> int:


        not_val_idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[not_val_idx] = nums[i]
                not_val_idx += 1
        nums = nums[0:not_val_idx]
        return not_val_idx



s = Solution()
ret = s.removeElement([0,1,2,2,3,0,4,2], 2)
print(f'ret {ret}')

