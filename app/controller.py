def chessBoard():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                newDict = {
                    "color": "white",
                    "class": "box"
                }
            else:
                newDict = {
                    "color": "black",
                    "class": "box"
                }
            board[i].append(newDict)
    return board