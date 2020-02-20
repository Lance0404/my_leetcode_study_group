"""
https://leetcode.com/problems/longest-palindrome/


Runtime: 24 ms, faster than 94.32% of Python3 online submissions for Longest Palindrome.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.
"""


class Solution:

    def longestPalindrome(self, s: str) -> int:

        def get_count_status(ss: str) -> dict:
            status = {}
            for i in ss:
                if i not in status:
                    status[i] = 1
                else:
                    status[i] += 1
            return status

        char_to_count = get_count_status(s)
        # print(char_to_count)

        # sum up all the even counts and every odd count with minus 1, but add 1 back in the end if at least one odd exist
        longest_count = 0
        odd_exist = False
        for k,v in char_to_count.items():
            if v % 2 == 0:
                longest_count += v
            else:
                odd_exist = True
                longest_count += v - 1
        if odd_exist:
            longest_count += 1

        return longest_count



s = Solution()
# ret = s.longestPalindrome('dccaccd')
# print(f'ret {ret}')
# ret = s.longestPalindrome('abccccdd')
# print(f'ret {ret}')
# ret = s.longestPalindrome('adam')
# print(f'ret {ret}')
ret = s.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth')
print(f'ret {ret}')

