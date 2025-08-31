class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r = [0] * 9
        c = [0] * 9
        b = [0] * 9
        e_c = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    test = 1 << (num - 1)
                    r[i] |= test
                    c[j] |= test
                    b[(i // 3) * 3 + (j // 3)] |= test
                else:
                    e_c.append((i, j))

        def backtrack(index):
            if index == len(e_c):
                return True
            i, j = e_c[index]
            b_i = (i // 3) * 3 + (j // 3)
            used_numbers = r[i] | c[j] | b[b_i]
            for num in range(1, 10):
                test = 1 << (num - 1)
                if not (used_numbers & test):
                    board[i][j] = str(num)
                    r[i] |= test
                    c[j] |= test
                    b[b_i] |= test
                    if backtrack(index + 1):
                        return True
                    board[i][j] = '.'
                    r[i] ^= test
                    c[j] ^= test
                    b[b_i] ^= test
            return False

        backtrack(0)