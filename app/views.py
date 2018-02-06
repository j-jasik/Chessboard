from flask_classy import FlaskView, route
from flask import render_template
from controller import *

class BaseView(FlaskView):
    route_base = '/'

    def index(self):
        board = chessBoard()
        #return render_template('index.html', **locals())
        return render_template("index.html", **locals())

    @route('/update-xml')
    def test(self):
        #return render_template('index.html', **locals())
        return "YAY"
