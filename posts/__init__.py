from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask import Blueprint, render_template

# Reutilize a instância global do db criada no run.py
from run import db

posts = Blueprint("posts", __name__)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    views = db.Column(db.Integer, default=0)


@posts.route("/")
def index():
    return render_template("index.html")
