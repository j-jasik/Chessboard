from flask_classy import FlaskView, route
from flask import render_template
from controller import *
import random

class BaseView(FlaskView):
    route_base = '/'

    def index(self):
        board = chessBoard('black')
        return render_template("index.html", **locals())

    @route('/change-color-board', methods=['post'])
    def change_color_board(self):
        colors = ['red','green','blue']
        return chessBoard(colors[random.randint(0,2)])
