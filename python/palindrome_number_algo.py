"""
https://leetcode.com/problems/palindrome-number/

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # else should be >= 0, so the minimum digit number is 1

        digit_num = 1
        z = x
        int_lst = []
        while z / 10 >= 1:
            digit_num += 1
            remainder = z % 10
            print(f'remainder {remainder}')
            int_lst.append(remainder)
            z = int((z - remainder) / 10)
        remainder = z % 10
        int_lst.append(remainder)
        # print(f'digit_num {digit_num}')
        # print(f'int_lst {int_lst}')
        # print(f'len int_lst: {len(int_lst)}')
        for _ in range(len(int_lst) // 2):
            print(_)
            if int_lst.pop() != int_lst.pop(0):
                return False
        return True


s = Solution()
ret = s.isPalindrome(-10)
print(f'ret {ret}')
ret = s.isPalindrome(10)
print(f'ret {ret}')
ret = s.isPalindrome(999)
print(f'ret {ret}')
ret = s.isPalindrome(99988999)
print(f'ret {ret}')
ret = s.isPalindrome(999878999)
print(f'ret {ret}')

