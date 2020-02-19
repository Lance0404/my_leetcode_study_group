"""
https://leetcode.com/problems/longest-common-prefix/

Input: ["flower","flow","flight"]
Output: "fl"

Runtime: 28 ms, faster than 88.08% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.

"""


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:

        def match_step(strs, shortest_item: str, step: int) -> str:
            s = shortest_item[0:step]
            print(s)
            all_str_match = True
            for j in strs:
                if not j.startswith(s):
                    all_str_match = False
                    break
            if all_str_match:
                return s
            return None

        if not strs:
            return ''
        # find the one with the shortest length
        shortest_len = shortest_idx = shortest_item = None
        for i in range(len(strs)):
            if not shortest_len or len(strs[i]) < shortest_len:
                shortest_len = len(strs[i])
                shortest_idx = i
                shortest_item = strs[i]

        print(f'shortest_len {shortest_len} shortest_idx {shortest_idx} shortest_item {shortest_item}')

        # loop through from the largest step to the shortest
        step = len(strs[shortest_idx])
        while step > 0:
            ret = match_step(strs, shortest_item, step)
            if ret:
                return ret
            step -= 1
        return ''






s = Solution()
ret = s.longestCommonPrefix(["flower","flow","flight"])
print(f'ret {ret}')
ret = s.longestCommonPrefix([])
print(f'ret {ret}')
ret = s.longestCommonPrefix(["ca","a"])
print(f'ret {ret}')
ret = s.longestCommonPrefix(["flower","flow","flight"])
print(f'ret {ret}')


