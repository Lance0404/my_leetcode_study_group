"""
https://leetcode.com/problems/roman-to-integer/

# ref : https://www.romannumerals.org/converter

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Runtime: 60 ms, faster than 14.93% of Python3 online submissions for Roman to Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
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
        self.thousand_ck_lst = ['MMM', 'MM', 'M']
        self.hundred_ck_lst = ['CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C']
        self.ten_ck_lst = ['XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X']
        self.one_ck_lst = ['IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']

    def romanToInt(self, s: str) -> int:
        def roman_to_int_foreach_digit(ss: str, to_check: list, upper: str, middle: str, step: str) -> (int, str):
            for i in to_check:
                if ss.startswith(i):
                    if upper and i.endswith(upper):
                        ret = self.symbol_to_value[upper] - self.symbol_to_value[step]
                    elif middle and i.startswith(middle):
                        ret = self.symbol_to_value[middle] + self.symbol_to_value[step] * (len(i) - 1)
                    elif middle and i.endswith(middle):
                        ret = self.symbol_to_value[middle] - self.symbol_to_value[step]
                    else:
                        ret = self.symbol_to_value[step] * len(i)
                    return ret, ss[len(i):]
            return 0, ss

        ret_int = 0

        converted_int, s = roman_to_int_foreach_digit(s, self.thousand_ck_lst, None, None, 'M')
        ret_int += converted_int
        print(f'ret_int {ret_int}, s {s}')

        converted_int, s = roman_to_int_foreach_digit(s, self.hundred_ck_lst, 'M', 'D', 'C')
        ret_int += converted_int
        print(f'ret_int {ret_int}, s {s}')

        converted_int, s = roman_to_int_foreach_digit(s, self.ten_ck_lst, 'C', 'L', 'X')
        ret_int += converted_int
        print(f'ret_int {ret_int}, s {s}')

        converted_int, s = roman_to_int_foreach_digit(s, self.one_ck_lst, 'X', 'V', 'I')
        ret_int += converted_int
        print(f'ret_int {ret_int}, s {s}')

        return ret_int


s = Solution()
ret = s.romanToInt('MCMXCIV') # M CM XC IV
print(f'ret {ret}') # 1994
ret = s.romanToInt('III') # M CM XC IV
print(f'ret {ret}') # 3

# a = 'abcd'
# print(a[2:])