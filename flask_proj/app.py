from flask import Flask, redirect, url_for


app=Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to this shitty app'

@app.route('/success/<int:score>')
def success(score):
    if score>50:
        return f'you have scored {score},hence you have passed'
    else:
        return f'you have scored {score},hence you have failed'


if __name__=='__main__':
    app.run()