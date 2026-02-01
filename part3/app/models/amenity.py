from app.models.base import BaseModel
from app.extensions import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    _name = db.Column("name", db.String(50), nullable=False)

    def __init__(self, name, description=""):
        self.name = name
        # We don't save description in DB for this simple model, 
        # but the init expects it for compatibility
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Amenity name cannot be empty")
        self._name = value
