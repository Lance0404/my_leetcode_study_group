"""
https://leetcode.com/problems/repeated-substring-pattern/

Runtime: 124 ms, faster than 35.08% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Repeated Substring Pattern.
very bad performance
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
      i = 1
      while i <= len(s)/2:

        if len(s) % i != 0:
          i += 1
          continue
        FAILED_CHECK = False
        x = 0
        while x <= len(s)-i:
          print(f'substr {s[0:i]}, i {i}, x {x}' )
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

"""
Runtime: 172 ms, faster than 21.95% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 14.4 MB, less than 99.99% of Python3 online submissions for Repeated Substring Pattern.
"""
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
      for i in range(1, len(s)):
        sub_str = s[:i]
        if s == sub_str*int(len(s)/i): return True
      return False

s = Solution2()
# ret = s.repeatedSubstringPattern('abababab')
# ret = s.repeatedSubstringPattern('abac')
# ret = s.repeatedSubstringPattern('aabaaba')
# ret = s.repeatedSubstringPattern('abab')
ret = s.repeatedSubstringPattern('abaababaab')

print(ret)