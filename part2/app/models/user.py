"""
User Model Module
"""
from app.models.base import BaseModel

class User(BaseModel):
    """
    Represents a user in the HBnB application.
    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """Initialize a new User instance."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

    @property
    def first_name(self):
        """Getter for first_name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Setter for first_name. Validates length."""
        if not value or len(value) > 50:
            raise ValueError("First name must be 50 characters or less")
        self._first_name = value

    @property
    def email(self):
        """Getter for email."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email. Validates simple format."""
        if not value or "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        self._email = value
