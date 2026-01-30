"""
BaseModel Module
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models in the HBnB application.
    Handles ID generation, timestamps, and safe serialization.
    """

    def __init__(self):
        """Initialize a new instance with UUID and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified."""
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def to_dict(self):
        """
        Convert the object to a dictionary.
        Excludes sensitive fields like password_hash.
        """
        result = {}

        for key, value in self.__dict__.items():
            # 🚫 Never expose password hashes
            if key == 'password_hash':
                continue

            # Convert datetime objects to ISO format
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value

        return result

