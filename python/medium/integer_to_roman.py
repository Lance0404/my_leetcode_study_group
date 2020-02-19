"""
https://leetcode.com/problems/integer-to-roman/

Runtime: 52 ms, faster than 48.44% of Python3 online submissions for Integer to Roman.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
"""


class Solution:
    def __init__(self):
        self.symbol_to_value = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        # in the order of upper, middle, step
        # the pattern is the same for every digit
        self.thousand_info = (None, None, 'M')
        self.hundred_info = ('M', 'D', 'C')
        self.ten_info = ('C', 'L', 'X')
        self.one_info = ('X', 'V', 'I')

        self.check_lst = []
        self.check_lst.append(self.one_info)
        self.check_lst.append(self.ten_info)
        self.check_lst.append(self.hundred_info)
        self.check_lst.append(self.thousand_info)

    def intToRoman(self, num: int) -> str:
        def each_int_to_roman(digit: int, idx: int) -> str:
            '''
            :param digit: a single digit
            :param idx: start from the right most digit
            :return: roman string
            '''
            info = self.check_lst[idx]
            ret = ''
            if digit == 0:
                pass
            elif digit == 1:
                ret += info[2]
            elif digit == 2:
                ret += info[2] * 2
            elif digit == 3:
                ret += info[2] * 3
            elif digit == 4:
                ret += info[2] + info[1]
            elif digit == 5:
                ret += info[1]
            elif digit == 6:
                ret += info[1] + info[2]
            elif digit == 7:
                ret += info[1] + info[2] * 2
            elif digit == 8:
                ret += info[1] + info[2] * 3
            elif digit == 9:
                ret += info[2] + info[0]
            return ret

        # I decided to start from the right most digit
        x = num

        ret_roman = ''
        # there will be at most 4 digits
        for i in range(4):
            ret_roman = each_int_to_roman(x % 10, i) + ret_roman
            x = x // 10
        return ret_roman


s = Solution()
ret = s.intToRoman(3)
print(f'ret {ret}')
ret = s.intToRoman(1994)
print(f'ret {ret}')



