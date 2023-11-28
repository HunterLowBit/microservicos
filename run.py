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
from users.models import User  # Assumindo que o modelo User está em users/models.py
from posts.models import Post  # Assumindo que o modelo Post está em posts/models.py

# Cria as tabelas
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
