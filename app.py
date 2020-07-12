from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dutyfirst!@localhost/mywebsite'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI']

# app.config['SQLALCHMEY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['mail']
        if db.session.query(User).filter(User.email == email).count() == 0:
        	data = User(email)
        	db.session.add(data)
        	db.session.commit()
        	send_mail(email)
        	return redirect('/')
        return redirect('/')


if __name__ == "__main__":
    app.run()
