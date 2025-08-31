class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Fill initial sets + track empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    ch = board[r][c]
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r//3)*3 + (c//3)].add(ch)
                else:
                    empties.append((r, c))

        def solve():
            if not empties:
                return True

            # Instead of sorting, find the best empty cell directly
            best_idx, best_options = -1, None
            for i, (r, c) in enumerate(empties):
                box_idx = (r//3)*3 + (c//3)
                options = {"1","2","3","4","5","6","7","8","9"} - rows[r] - cols[c] - boxes[box_idx]
                if best_options is None or len(options) < len(best_options):
                    best_idx, best_options = i, options
                    if len(best_options) == 1:  # early stop if only 1 option
                        break

            r, c = empties.pop(best_idx)
            box_idx = (r//3)*3 + (c//3)

            for ch in best_options:
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[box_idx].add(ch)

                if solve():
                    return True

                # Backtrack
                board[r][c] = '.'
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[box_idx].remove(ch)

            empties.insert(best_idx, (r, c))
            return False

        solve()