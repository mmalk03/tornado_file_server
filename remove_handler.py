import os
import string

import tornado


class RemoveHandler(tornado.web.RequestHandler):
    remove_dir = ""

    def initialize(self, remove_dir):
        self.remove_dir = remove_dir
        if not str(remove_dir).endswith('/'):
            self.remove_dir += '/'

    def post(self, path):
        print('Removed: ' + self.remove_dir + path)
        os.remove(self.remove_dir + path)
        self.redirect('/browse/')
