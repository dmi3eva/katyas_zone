from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Settings for test
HOST = "localhost"
PORT = "5433"
DB_NAME = "katya_db"
USER = "katya"
PASSWORD = "100542"


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////tmp/{DB_NAME}.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
admin = User(username='admin', email='admin@example.com')
guest = User(username=USER, email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
# app.run(host=HOST, port=PORT)