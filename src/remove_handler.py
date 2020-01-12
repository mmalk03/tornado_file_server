import os

import tornado


class RemoveHandler(tornado.web.RequestHandler):
    remove_dir = ""

    def initialize(self, remove_dir):
        self.remove_dir = remove_dir
        if not str(remove_dir).endswith('/'):
            self.remove_dir += '/'

    def post(self, path):
        path_to_file = self.remove_dir + path
        os.remove(path_to_file)
        print('Removed: ' + path_to_file)
        self.redirect('/')
