"""
https://leetcode.com/problems/implement-strstr/

Runtime: 24 ms, faster than 95.46% of Python3 online submissions for Implement strStr().
Memory Usage: 14.1 MB, less than 8.00% of Python3 online submissions for Implement strStr().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      if not len(needle):
        return 0
      if needle not in haystack:
        return -1

      # edge cases handled above
      for i in range(len(haystack)):
        for j in range(i+len(needle), len(haystack)+1):
          if haystack[i:j] == needle:
            # return the first occurance
            return i


s = Solution()
ret = s.strStr('aaaaaaaaaaaaaaaabc', 'ab')
print(ret)
