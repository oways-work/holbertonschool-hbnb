"""
User Model Module
"""

from app.models.base import BaseModel
from app.extensions import bcrypt


class User(BaseModel):
    """
    Represents a user in the HBnB application.
    """

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = None
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    def set_password(self, password):
        """Hash and store the password"""
        self.password_hash = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

    def check_password(self, password):
        """Verify a password"""
        return bcrypt.check_password_hash(self.password_hash, password)

