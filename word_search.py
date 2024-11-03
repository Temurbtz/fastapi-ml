def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = '#'

        found = (backtrack(r + 1, c, index + 1) or
                 backtrack(r - 1, c, index + 1) or
                 backtrack(r, c + 1, index + 1) or
                 backtrack(r, c - 1, index + 1))

        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True

    return False

word_exists = exist([["A", "B", "C", "E"],
                      ["S", "F", "C", "S"],
                      ["A", "D", "E", "E"]], "ABCCED")
print(word_exists)  
