import uuid
from datetime import datetime
from app.extensions import db

class BaseModel(db.Model):
    __abstract__ = True  # Tells SQLAlchemy not to create a table for this class

    # UUID is standard for ID, String(36) holds the UUID format
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        """Saves the current instance to the database."""
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        """Updates the instance with dictionary data and saves."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        """Deletes the current instance from the database."""
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        result = self.__dict__.copy()
        # Remove SQLAlchemy internal state
        if "_sa_instance_state" in result:
            del result["_sa_instance_state"]
        # Remove protected attributes (like _password_hash)
        result = {k: v for k, v in result.items() if not k.startswith('_')}
        
        # Convert datetime objects to strings
        result['created_at'] = self.created_at.isoformat() if self.created_at else None
        result['updated_at'] = self.updated_at.isoformat() if self.updated_at else None
        return result
