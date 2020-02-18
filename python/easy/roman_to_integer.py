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

I 1
II 2
III 3
IV 4
V 5
VI 6
VII 7
VIII 8
IX 9

X 10
XX 20
XXX 30
XL 40
L 50
LX 60
LXX 70
LXXX 80
XC 90

C 100
CC 200
CCC 300
CD 400
D 500
DC 600
DCC 700
DCCC 800
CM 900

M 1000
MM 2000
MMM 3000

I to MMM CM XC IX

4th digit M
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_value = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        thousand_ck_lst = ['MMM', 'MM', 'M']
        hundred_ck_lst = ['CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C']
        ten_ck_lst = ['XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X']
        one_ck_lst = ['IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I']

        def roman_to_int_foreach_digit(ss: str, to_check: list, upper: str, middle: str, step: str) -> (int, str):
            for i in to_check:
                if ss.startswith(i):
                    if i.endswith(upper):
                        ret = symbol_to_value[upper] - symbol_to_value[step]
                    elif i.startswith(middle):
                        ret = symbol_to_value[middle] + symbol_to_value[step] * (len(i) - 1)
                    elif i.endswith(middle):
                        ret = symbol_to_value[middle] - symbol_to_value[step]
                    else:
                        ret = symbol_to_value[step] * len(i)
                    ss = ss[len(i):]
                    return ret, ss
            return 0, ss

        ret_int = 0
        for i in thousand_ck_lst:
            if s.startswith(i):
                # each can only be 'M'
                ret_int += symbol_to_value['M'] * len(i)
                s = s[len(i):]
                break
        print(f'ret_int {ret_int}, s {s}')

        converted_int, s = roman_to_int_foreach_digit(s, hundred_ck_lst, 'M', 'D', 'C')
        ret_int += converted_int
        print(f'ret_int {ret_int}, s {s}')

        converted_int, s = roman_to_int_foreach_digit(s, ten_ck_lst, 'C', 'L', 'X')
        ret_int += converted_int
        print(f'ret_int {ret_int}, s {s}')

        converted_int, s = roman_to_int_foreach_digit(s, one_ck_lst, 'X', 'V', 'I')
        ret_int += converted_int
        print(f'ret_int {ret_int}, s {s}')
        return ret_int


s = Solution()
# ret = s.romanToInt('MCMXCIV') # M CM XC IV
# print(f'ret {ret}') # 1994
ret = s.romanToInt('III') # M CM XC IV
print(f'ret {ret}') # 3