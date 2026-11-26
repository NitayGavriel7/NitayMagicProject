import os
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/magic_zone')
def magic_zone():
    return render_template('magic_zone.html')

@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)