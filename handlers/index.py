# coding:utf-8

import tornado.web
import solver
import message

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        result = [[0 for col in xrange(9)] for row in xrange(9)]
        self.render("index.html", message=message.exam_msg, result=result)

    def post(self):
        board = []
        result = []
        file_metas = self.request.files['file']
        for meta in file_metas:
            board = meta['body'].split()

        for element in board:
            result.append(map(int, element.split(',')))

        msg, result = solver.get_result(result)

        self.render("index.html", message=msg, result=result)