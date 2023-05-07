from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_BINDS'] = {
    'messages': 'sqlite:///message.db'
}

db = SQLAlchemy(app)



class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' %self.id

class Message(db.Model):
    __bind_key__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    Surname = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Message %r>' % self.Name


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/weekend')
def weekend():
    return render_template("weekend.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page:' + name + "-" + str(id)

if __name__ == '--main__':
    app.run(debug=True)
