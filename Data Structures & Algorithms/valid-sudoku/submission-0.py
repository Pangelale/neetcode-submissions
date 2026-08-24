class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        position = {}

        for i in range(len(board)):
            for j in range(len(board)):
                current = board[i][j]
                box = (i // 3, j // 3)

                if current == ".":
                    continue

                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if box not in position:
                    position[box] = set()

                if current in rows[i] or current in cols[j] or current in position[box]:
                    return False
                else:
                    rows[i].add(current)
                    cols[j].add(current)
                    position[box].add(current)
     
        return True