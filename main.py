from flask import Flask, request
import helpers
from caesar import encrypt

import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
app = Flask(__name__)
app.config['DEBUG'] = True





@app.route("/", methods=['GET', 'POST'])
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

''' def encrpyt():
    if request.method == 'POST':
        rot = request.form.get['rot']
        text = request.form['textarea']
        encryptedText = encrypt(text, rot)
    return  
'''

app.run()