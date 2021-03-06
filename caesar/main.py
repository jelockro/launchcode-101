from flask import Flask, request, redirect
import helpers
from caesar import encrypt

import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route("/", methods=['POST'])
def caesar(): 
    rot = int(request.form.get('rot', 0))
    text = request.form.get('text', '')
    encryptedText = encrypt(text, rot)
    template = jinja_env.get_template('form.html')
    return template.render(text=encryptedText)

app.run()