"""
https://leetcode.com/problems/subarray-sum-equals-k/

I implemented the solution 4

Runtime: 112 ms, faster than 80.19% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 15.1 MB, less than 96.00% of Python3 online submissions for Subarray Sum Equals K.
"""


class Solution:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        cnt = 0
        sum = 0
        sum_hash = {}
        loop_cnt = 0  # just for checking the loop count
        for i in nums:
            loop_cnt += 1
            sum += i
            diff = sum - k

            if diff == 0:
                # which means from there is a subarray with sum == k from the first node to the current node
                cnt += 1
            if diff in sum_hash:
                # which means there is at least one subarray with sum == k
                # in between a previous node and the current node
                cnt += sum_hash[diff]

            # use a hash to accumulate the count for all unique sum values
            if sum not in sum_hash:
                sum_hash[sum] = 1
            else:
                sum_hash[sum] += 1

            print(f'i {i} loop {loop_cnt} sum {sum} diff {diff} sum_hash {sum_hash} cnt {cnt}')
        return cnt


sol = Solution()
ret = sol.subarraySum([1,1,1], 2)
print(f'ret {ret}') # 2
ret = sol.subarraySum([1,2,3], 3)
print(f'ret {ret}') # 2
ret = sol.subarraySum([1,2,1,2,1],3)
print(f'ret {ret}') # 4
ret = sol.subarraySum([1],0)
print(f'ret {ret}') # 0
