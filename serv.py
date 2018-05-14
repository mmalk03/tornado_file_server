import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
uploads_dir = "uploads/"
uploaded_file = None


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/login", LoginHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': r'uploads'})
            # home/qwark/virtualenvironment/tornado/
        ]
        tornado.web.Application.__init__(self, handlers, cookie_secret="qwe123")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload_form.html")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        uploaded_file = self.request.files['file1'][0]
        self.redirect("/login")


class LoginHandler(UploadHandler):
    def get(self):
        file = open("login_form.html", 'r')
        self.write(file.read())

    def post(self):
        name = self.get_argument("name")
        password = self.get_argument("password")
        if name == 'qwe' and password == '123':
            original_filename = uploaded_file['filename']
            output_file = open(uploads_dir + original_filename, 'wb')
            output_file.write(uploaded_file['body'])
            self.finish("file" + original_filename + " is uploaded")
        else:
            self.finish("Wrong credentials")


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
