from app.extensions import db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class SQLAlchemyRepository:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        """Get an object by ID"""
        return self.model.query.get(id)

    def get_all(self):
        """Get all objects"""
        return self.model.query.all()

    def add(self, obj):
        """Add a new object to the database"""
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, obj_id, data):
        """Update an object by ID"""
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            db.session.commit()
            return obj
        return None

    def delete(self, obj_id):
        """Delete an object by ID"""
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
            return True
        return False

    def get_by_attribute(self, attr_name, attr_value):
        """Get an object by a specific attribute (e.g., email)"""
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
