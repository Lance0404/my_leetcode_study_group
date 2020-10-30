"""
https://leetcode.com/problems/repeated-string-match/

Runtime: 144 ms, faster than 33.78% of Python3 online submissions for Repeated String Match.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Repeated String Match.
"""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
      # print(f'a: {a}, length {len(a)}')
      # print(f'b: {b}, length {len(b)}')
      current_a = a
      while len(current_a) <= len(a)*2 + len(b):
        # print(f'{current_a} {len(current_a)}')
        if b in current_a:
          return int(len(current_a)/len(a))
        else:
          current_a += a
      return -1

s = Solution()
# ret = s.repeatedStringMatch('ab', 'ababab')
ret = s.repeatedStringMatch('abc', 'cabcabca')
print(ret)
