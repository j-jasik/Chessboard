from flask import render_template

def chessBoard(color1, color2):
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                newDict = {
                    "color": color1,
                    "class": "box"
                }
            else:
                newDict = {
                    "color": color2,
                    "class": "box"
                }
            board[i].append(newDict)
    return render_template("board.html", **locals())