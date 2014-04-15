from flask import Flask
app = Flask(__name__,static_folder='/home/tlatorre/Documents/phy237/tensor/_build/html')

from os.path import join

@app.route('/')
@app.route('/<filename>')
@app.route('/_static/<filename>', defaults={'static': True})
@app.route('/_images/<filename>', defaults={'images': True})
def tensor(filename='index.html', static=False, images=False):
    if static:
        path = join('_static',filename)
    elif images:
        path = join('_images',filename)
    else:
        path = filename

    return app.send_static_file(path)
