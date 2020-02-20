"""
https://leetcode.com/problems/longest-palindrome/


Time Limit Exceeded
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:

        def can_build_palindrome(ss: str) -> bool:
            # this is a expensive calculation
            # if two char with odd count than it can not built a palindrome
            ck_dic = {}
            for j in ss:
                if j not in ck_dic:
                    ck_dic[j] = 1
                else:
                    ck_dic[j] += 1

            # print(ck_dic)
            odd_cnt = 0
            for v in ck_dic.values():
                if v % 2 == 1:
                    odd_cnt += 1
                if odd_cnt > 1:
                    return False
            print(f'ss {ss}')
            return True

        len_s = len(s)  # str is assigned by value, not reference
        len_x = len_s

        if len_x > 1010:
            return 0
        while len_x > 0:
            # loop through all the sub string of given length, starting from the largest
            for i in range(len_s):
                end_idx = i + len_x
                if end_idx > len_s:
                    break
                sub_s = s[i:i + len_x]
                if can_build_palindrome(sub_s):
                    return len(sub_s)
            len_x -= 1
        return 0


s = Solution()
# ret = s.longestPalindrome('dccaccd')
# print(f'ret {ret}')
# ret = s.longestPalindrome('abccccdd')
# print(f'ret {ret}')
# ret = s.longestPalindrome('adam')
# print(f'ret {ret}')
ret = s.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth')
print(f'ret {ret}')
