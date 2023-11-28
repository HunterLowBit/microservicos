from flask import Blueprint, render_template
from datetime import datetime
from run import db
from .models import Post

posts = Blueprint("posts", __name__)


@posts.route("/")
def index():
    return render_template("index.html")
