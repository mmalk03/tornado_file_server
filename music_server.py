import argparse

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from index_handler import IndexHandler
from remove_handler import RemoveHandler
from tornado_app import MyTornadoApplication
from upload_handler import UploadHandler

defaults = {
    'port': 8888,
    'username': 'qwe',
    'password': '123',
    'file_serve_dir': 'music',
    'file_upload_dir': 'music',
    'static_path': 'static'
}


def main(args):
    handlers = [
        (r"/", IndexHandler, {'serve_dir': args.serve_dir}),
        (r"/upload/", UploadHandler, {'upload_dir': args.upload_dir}),
        (r"/remove/(.*)", RemoveHandler, {'remove_dir': args.serve_dir}),
        (r"/download/(.*)", tornado.web.StaticFileHandler, {'path': args.serve_dir})
    ]
    settings = {
        "static_path": args.static_path
    }
    print('Starting music server on port {}'.format(args.port))
    http_server = tornado.httpserver.HTTPServer(MyTornadoApplication(handlers, settings))
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            'Start a Tornado server to serve, upload and play music files from/to given directory.'))
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
    parser.add_argument(
        '--static-path', type=str, default=defaults['static_path'],
        help='Directory where static files are (e.g. javascript or css).')
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
