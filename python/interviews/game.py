"""
井字遊戲
"""

from typing import List


class Game:
    def __init__(self, n) -> None:
        self.n = n
        self.table = [[False for _ in range(n)] for _ in range(n)]
        for i in self.table:
            print(i)
        print(' ================ after init ================= ')

    def insert_table(self, table: List[List]):
        """
        for test
        """
        self.table = table
        self.show()
        self.analyze()

    def insert(self, pos: tuple, key: "X or O"):
        """
        pos (row, col)
        """
        row, col = pos
        self.table[row][col] = key
        self.show()
        self.analyze()

    def analyze(self):
        if self.check_win():
            print('bingo')
        elif self.is_draw():
            print('draw game')
        else:
            print('please continue')        

    def is_draw(self) -> bool:
        for i in self.table:
            for j in i:
                if j:
                    pass
                else:
                    return False
        return True

    def show(self):
        for i in self.table:
            print(i)
        print(' ================ after a show ================= ')

    def check_win(self) -> bool:
        """
        True means win
        False means no win

        1. & 2. is similar but I tried with different coding style
        """
        # 1. fix col, check row from top to button
        row = col = 0
        while col < self.n - 1:
            if not (cur := self.table[row][col]):
                col += 1
                continue
            while row < self.n - 1 and self.table[row + 1][col] == cur:
                row += 1
            if row == self.n - 1:
                return True
            row = 0
        
        # 2. fix row, check col from left to right
        row = col = 0
        while row < self.n - 1:
            if (cur := self.table[row][col]):
                while col < self.n - 1:
                    if self.table[row][col + 1] == cur:
                        col += 1
                    else:
                        col = 0
                        break
            if col == self.n - 1:
                return True
            row += 1

        # 3. check diagonal, from top left to buttom right 
        row = col = 0
        if (cur := self.table[row][col]):
            while row < self.n - 1:
                if self.table[row + 1][col + 1] == cur:
                    row += 1
                    col += 1
                else:
                    break
        if row == self.n - 1:
            return True

        # 4. check diagonal, from bottom left to top right 
        row, col = self.n - 1, 0
        if (cur := self.table[row][col]):
            while row > 0:
                if self.table[row - 1][col + 1] == cur:
                    row -= 1
                    col += 1
                else:
                    break
        if row == 0:
            return True


g = Game(3)
# g.insert((0,0), 'X')
# g.insert((2,2), 'Y')

g.insert_table(
    [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['X', 'X', 'O'],
    ]
)
# bingo

# g.insert_table(
#     [
#         ['X', False, 'X'],
#         ['X', 'X', False],
#         [False, False, False],
#     ]
# )
# please continue

# g.insert_table(
#     [
#         ['X', False, 'X'],
#         ['X', 'X', False],
#         ['O', False, False],
#     ]
# )
# please continue

# g.insert_table(
#     [
#         ['X', 'O', 'X'],
#         ['X', 'X', 'O'],
#         ['O', 'X', 'O'],
#     ]
# )
# draw game