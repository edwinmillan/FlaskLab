from flask import render_template
from microblog import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Bob'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user = user, posts = posts)
