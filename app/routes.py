from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/welcome')
def index():
    user = {'username': 'Frank'}
    return render_template('index.html',title='LSY',user=user)

def welcome():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
