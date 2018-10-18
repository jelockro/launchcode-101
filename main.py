from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="" id="usrform" method="POST">
            Rotate by: 
            <input type="text" name="rot" value="0"><br>
             <textarea name="text" rows="10" cols="70" form="usrform"></textarea>
            <input type="submit" value="Submit Request">
        </form>
       
    </body>
</html>
'''



@app.route("/")
def index():
    return form

app.run()