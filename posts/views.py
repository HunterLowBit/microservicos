from flask import render_template, Blueprint
from .models import Post, db

posts = Blueprint("posts", __name__)


@posts.route("/")
def index():
    return render_template("index.html")
