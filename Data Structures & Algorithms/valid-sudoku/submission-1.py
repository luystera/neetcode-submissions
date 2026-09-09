class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # solution using a single hashset
        seen = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                
                # create unique keys for the row, column, and box
                row_key = f"row{i}{val}"
                col_key = f"col{val}{j}"
                box_key = f"box{i//3}{j//3}{val}"

                # check for duplicates
                if (row_key in seen) or (col_key in seen) or (box_key in seen):
                    return False

                # add the keys to the hashset
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True


