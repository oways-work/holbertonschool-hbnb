from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Initialize the extensions (but don't bind them to the app yet)
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
