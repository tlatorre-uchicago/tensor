from flask import Flask
app = Flask(__name__,static_folder='/home/tlatorre/Documents/phy237/tensor/_build/html')

from os.path import join

@app.route('/')
@app.route('/<filename>')
@app.route('/<dir>/<filename>')
def tensor(dir='',filename='index.html'):
    path = join(dir,filename)
    return app.send_static_file(path)
