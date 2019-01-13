from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'


@app.route('/page1')
def page1() -> str:
    return 'This is the page 1'


@app.route('/page2')
def page2() -> str:
    return 'This is the page 2'


@app.route('/page3')
def page3() -> str:
    return 'This is the page 3'


@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'You are now logged out'


@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in'
    else:
        return 'You are NOT logged in'


if __name__ == '__main__':
    app.run(debug=True)