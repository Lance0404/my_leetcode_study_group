"""
https://leetcode.com/problems/longest-palindromic-substring/

Runtime: 1720 ms, faster than 48.56% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # there two types of palindrome: odd and even

        # init with the first idx
        longest_start_idx = 0
        longest_end_idx = 0
        longest_length = longest_end_idx - longest_start_idx + 1  # 1
        i = 0  # starting from the first index
        while i < len(s):
            odd_prev_idx = even_prev_idx = odd_next_idx = even_next_idx = i
            odd_match = even_match = True  # init both as True
            # do the odd and even palindrome search in one loop together
            loop_i = 0  # store the loop count
            while odd_match or even_match:
                if odd_match and odd_prev_idx - 1 >= 0 and odd_next_idx + 1 <= len(s) - 1 \
                        and s[odd_prev_idx - 1] == s[odd_next_idx + 1]:
                    odd_prev_idx -= 1
                    odd_next_idx += 1
                else:
                    odd_match = False

                if even_match and (
                        even_prev_idx if not loop_i else even_prev_idx - 1) >= 0 and even_next_idx + 1 <= len(s) - 1 \
                        and s[even_prev_idx if not loop_i else even_prev_idx - 1] == s[even_next_idx + 1]:
                    even_prev_idx -= 0 if not loop_i else 1
                    even_next_idx += 1
                else:
                    even_match = False
                # print(
                #     f'i {i} loop_i {loop_i}, odd_prev_idx {odd_prev_idx} odd_next_idx {odd_next_idx} odd_match {odd_match},'
                #     f' even_prev_idx {even_prev_idx} even_next_idx {even_next_idx} even_match {even_match}')

                loop_i += 1

            cur_odd_length = odd_next_idx - odd_prev_idx + 1
            cur_even_length = even_next_idx - even_prev_idx + 1

            if cur_odd_length > cur_even_length and cur_odd_length > longest_length:
                longest_length = cur_odd_length
                longest_start_idx = odd_prev_idx
                longest_end_idx = odd_next_idx
            elif cur_even_length > cur_odd_length and cur_even_length > longest_length:
                longest_length = cur_even_length
                longest_start_idx = even_prev_idx
                longest_end_idx = even_next_idx
            # print(
            #     f'i {i} cur_odd_length {cur_odd_length} cur_even_length {cur_even_length} longest_length {longest_length}')
            # move the checking index to the idx of the rightmost item in the palindrome
            # i = longest_end_idx if longest_end_idx > i else i + 1
            i = i + 1
        return s[longest_start_idx:longest_end_idx + 1]  # get sub string


s = Solution()
# ret = s.longestPalindrome('babad')
# print(f'ret {ret}')
# ret = s.longestPalindrome('abb')
# print(f'ret {ret}')
ret = s.longestPalindrome('bb')
print(f'ret {ret}')  # bb
# ret = s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
# print(f'ret {ret}')
# ret = s.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(f'ret {ret}')
# ret = s.longestPalindrome('ababababababa')
# print(f'ret {ret}')  # "ababababababa"
# ret = s.longestPalindrome('tattarrattat')
# print(f'ret {ret}')  # "tattarrattat"
# ret = s.longestPalindrome('cbbd')
# print(f'ret {ret}')  # "bb"
