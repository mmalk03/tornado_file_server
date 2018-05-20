import tornado


class UploadHandler(tornado.web.RequestHandler):
    username = ""
    password = ""
    upload_dir = ""

    def initialize(self, upload_dir):
        self.upload_dir = upload_dir
        if not str(upload_dir).endswith('/'):
            self.upload_dir += '/'

    # TODO: display login dialog
    def post(self):
        uploaded_file = self.request.files['uploaded_file'][0]
        original_filename = uploaded_file['filename']
        if original_filename.endswith('.mp3'):
            output_file = open(self.upload_dir + original_filename, 'wb')
            output_file.write(uploaded_file['body'])
            print('Uploaded: ' + original_filename)
            self.redirect('/')
        else:
            print('Wrong format')
            self.redirect('/')

    def post_old(self):
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
