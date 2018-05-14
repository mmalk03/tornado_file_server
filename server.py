import argparse

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from serve_handler import ServeHandler
from tornado_app import MyTornadoApplication
from upload_handler import UploadHandler

defaults = {
    'port': 8888,
    'username': 'qwe',
    'password': '123',
    'file_serve_dir': 'uploads',
    'file_upload_dir': 'uploads'
}


def main(args):
    handlers = [
        (r"/", UploadHandler, {'username': args.username, 'password': args.password, 'upload_dir': args.upload_dir}),
        (r"/browse/", ServeHandler, {'serve_dir': args.serve_dir}),
        (r"/download/(.*)", tornado.web.StaticFileHandler, {'path': args.serve_dir})
    ]
    print('Starting server on port {}'.format(args.port))
    http_server = tornado.httpserver.HTTPServer(MyTornadoApplication(handlers))
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()

    # path = os.getcwd() + '/' + defaults[;]


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            'Start a Tornado server to serve and upload files from/to given directory.'))
    parser.add_argument(
        '--port', type=int, default=defaults['port'],
        help='Port on which to run server.')
    parser.add_argument(
        '--username', type=str, default=defaults['username'],
        help='Username required for authentication.')
    parser.add_argument(
        '--password', type=str, default=defaults['password'],
        help='Password required for authentication.')
    parser.add_argument(
        '--serve-dir', type=str, default=defaults['file_serve_dir'],
        help='Directory from which to serve files.')
    parser.add_argument(
        '--upload-dir', type=str, default=defaults['file_upload_dir'],
        help='Directory to which upload files.')
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
