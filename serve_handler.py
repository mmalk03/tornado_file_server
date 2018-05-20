import os

import tornado


class ServeHandler(tornado.web.RequestHandler):
    serve_dir = ""

    def initialize(self, serve_dir):
        self.serve_dir = serve_dir
        if str(serve_dir).endswith('/'):
            self.serve_dir = self.serve_dir[:-1]

    def get(self):
        print('Get')
        files = self.get_available_files()
        self.finish(self.get_html(files))

    @staticmethod
    def get_html(files):
        html = """
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Directory Contents</title>
</head>
<body>
<h1>Directory Contents</h1>
    <table>
      <thead>
        <tr>
          <th>Filename</th>
        </tr>
      </thead>
      <tbody>
      """
        for file in files:
            html = html + "<tr><td>" \
                          """<form action="http://localhost:8888/remove/""" + file + """" method="post">""" \
                          """<input type="submit" value="X"/>""" \
                          """<a href="http://localhost:8888/download/""" + file + """">""" + file + "</a></form></td></tr>\n"
        html += """
      </tbody>
    </table>
    <form action="http://localhost:8888/"><input type="submit" value="Uploads"/></form>
</body>
</html>
        """
        return html

    def get_available_files(self):
        files = []
        for (root, directories, file_names) in os.walk(self.serve_dir):
            for file_name in file_names:
                files.append(file_name)
        return files
