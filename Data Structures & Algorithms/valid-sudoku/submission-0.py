class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # loop through all the rows, cols, and squares in the board
        # boxes are a special case, they need to be initialized outside
        boxes = [set() for _ in range(9)] # 9 empty sets, 1 for each box
        for i in range(9):
            # hashsets for the current row and col
            curr_row = set()
            curr_col = set()
            for j in range(9):
                # calculate which box we are currently in
                box_index = (i // 3) * 3 + (j // 3)
                # check if there is a dupe in the row or box
                if board[i][j] != '.':
                    # check for row
                    if board[i][j] in curr_row:
                        return False
                    curr_row.add(board[i][j])
                    # check for box
                    if board[i][j] in boxes[box_index]:
                        return False
                    boxes[box_index].add(board[i][j])
                # check if there is a dupe in the col
                if board[j][i] != '.':
                    if board[j][i] in curr_col:
                        return False
                    curr_col.add(board[j][i])
        return True


