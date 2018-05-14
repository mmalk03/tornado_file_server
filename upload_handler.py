import tornado


class UploadHandler(tornado.web.RequestHandler):
    username = ""
    password = ""
    upload_dir = ""

    def initialize(self, username, password, upload_dir):
        self.username = username
        self.password = password
        self.upload_dir = upload_dir
        if not str(upload_dir).endswith('/'):
            self.upload_dir += '/'

    def get(self):
        self.render("upload_form.html")

    def post(self):
        input_name = self.get_argument("name")
        print('Provided name: ' + input_name)
        input_password = self.get_argument("password")
        print('Provided password: ' + input_password)
        if input_name == self.username and input_password == self.password:
            print('Access granted')
            uploaded_file = self.request.files['uploaded_file'][0]
            original_filename = uploaded_file['filename']

            output_file = open(self.upload_dir + original_filename, 'wb')
            output_file.write(uploaded_file['body'])

            self.finish("file " + original_filename + " is uploaded")
            print('Upload successful')
        else:
            print('Access denied')
            self.finish("Wrong credentials")
