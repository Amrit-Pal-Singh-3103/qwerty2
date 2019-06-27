from app import app
@app.route('/in')
def index():
    user={'username':'epic_gamer'}
    return '''
html
head
title homepage-micro_blog title
/head
body
h1 hello, '''+ user['username'] + '''! /h1
body
html'''

 
