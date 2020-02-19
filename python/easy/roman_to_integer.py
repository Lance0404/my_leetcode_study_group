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
        self.thousand_tup = ('MMM', 'MM', 'M')
        self.hundred_tup = ('CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C')
        self.ten_tup = ('XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X')
        self.one_tup = ('IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I')

        # in the order of upper, middle, step
        self.thousand_info = (None, None, 'M')
        self.hundred_info = ('M', 'D', 'C')
        self.ten_info = ('C', 'L', 'X')
        self.one_info = ('X', 'V', 'I')

        # prepare data set that aim to process from the leftmost digit
        self.check_lst = []
        self.check_lst.append((self.thousand_tup, self.thousand_info))
        self.check_lst.append((self.hundred_tup, self.hundred_info))
        self.check_lst.append((self.ten_tup, self.ten_info))
        self.check_lst.append((self.one_tup, self.one_info))
        # print(self.check_lst)

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

        # I decided to process from left to right
        ret_int = 0

        for i in self.check_lst:
            a, b = roman_to_int_foreach_digit(s, i[0], i[1][0], i[1][1], i[1][2])
            # print(f'a {a}, b {b}')
            s = b
            ret_int += a
        return ret_int


s = Solution()
ret = s.romanToInt('MCMXCIV') # M CM XC IV
print(f'ret {ret}') # 1994
ret = s.romanToInt('III') # M CM XC IV
print(f'ret {ret}') # 3
