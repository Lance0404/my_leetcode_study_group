"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array

Runtime: 84 ms, faster than 76.93% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        # the first index no need to be checked
        i = 0
        dedup_idx = 0
        while i + 1 <= len(nums) - 1:
            if nums[i] != nums[i+1]:
                dedup_idx += 1
                nums[dedup_idx] = nums[i+1]
            i += 1
        nums = nums[:dedup_idx + 1]
        return len(nums)


s = Solution()
ret = s.removeDuplicates([1,1,2])
print(f'ret {ret}')
ret = s.removeDuplicates([1,1,2,3,3])
print(f'ret {ret}')
