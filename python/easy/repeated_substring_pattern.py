"""
https://leetcode.com/problems/repeated-substring-pattern/

Runtime: 244 ms, faster than 14.73% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Repeated Substring Pattern.

very bad performance
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
      i = 1
      while i <= len(s)/2:
        FAILED_CHECK = False
        x = 0
        while x <= len(s)-i:
          # print(f'substr {s[0:i]}, i {i}, x {x}' )
          if s.startswith(s[0:i], x):
            x += i
          else:
            FAILED_CHECK = True
            break

        i += 1
        if FAILED_CHECK or x != len(s):
          continue
        else:
          return True

      return False

s = Solution()
# ret = s.repeatedSubstringPattern('abababab')
# ret = s.repeatedSubstringPattern('abac')
ret = s.repeatedSubstringPattern('aabaaba')
# ret = s.repeatedSubstringPattern('abab')
print(ret)