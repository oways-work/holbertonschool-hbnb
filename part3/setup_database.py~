from app import create_app, db
# Explicitly import models so they are registered with SQLAlchemy
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
    print(f"   Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
