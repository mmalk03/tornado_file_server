import os

import tornado


class IndexHandler(tornado.web.RequestHandler):
    serve_dir = ""

    def initialize(self, serve_dir):
        self.serve_dir = serve_dir
        if str(serve_dir).endswith('/'):
            self.serve_dir = self.serve_dir[:-1]

    def get(self):
        self.render("static/index.html", files=self.get_available_files())

    def get_available_files(self):
        files = []
        for (root, directories, file_names) in os.walk(self.serve_dir):
            for file_name in file_names:
                files.append(file_name)
        return files
