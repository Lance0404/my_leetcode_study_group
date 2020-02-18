"""
https://leetcode.com/problems/reverse-integer/submissions/

Runtime: 36 ms, faster than 18.30% of Python3 online submissions for Reverse Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.

"""


class Solution:

    def reverse(self, x: int) -> int:
        def constraint_with_scope(x: int) -> bool:
            if (2 ** 31) - 1 >= x >= (0 - (2 ** 31)):
                return x
            return 0

        def is_negative(x: int) -> bool:
            if x < 0:
                return True
            return False

        def reverse_integer(x: int) -> int:
            int_str_lst = list(str(x))
            reverse_int_str_lst = ''
            zero_from_right = False
            for i in range(len(int_str_lst)):
                right_most = int_str_lst.pop()
                if int(right_most) == 0 and zero_from_right is False:
                    continue
                zero_from_right = True
                reverse_int_str_lst += right_most
            # print(f'before {x}\n'
            #       f'after  {reverse_int_str_lst}')
            return int(reverse_int_str_lst)

        if not constraint_with_scope(x) or x == 0:
            return 0
        if is_negative(x):
            x = 0 - x  # make it positive
            return constraint_with_scope(0 - reverse_integer(x))
        return constraint_with_scope(reverse_integer(x))


s = Solution()
ret = s.reverse(2**31 -1)
print(f'ret {ret}')

ret = s.reverse(-10200)
print(f'ret {ret}')

ret = s.reverse(1534236469)
print(f'ret {ret}')

