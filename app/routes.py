from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cris'}
    posts = [
        {
            'author': {'username': 'Marina'},
            'body': 'Beautiful day in Towerplane!'
        },
        {
            'author': {'username': 'Pablo'},
            'body': 'I wanna play La Caja!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
