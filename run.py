from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_BINDS"] = {
    "users": "sqlite:///users.db",
    "posts": "sqlite:///posts.db",
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Import seus modelos aqui
from users.models import User
from posts.models import Post

# Registre os blueprints aqui
from users.views import users
from posts.views import posts

app.register_blueprint(users)
app.register_blueprint(posts)

# Cria as tabelas
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
