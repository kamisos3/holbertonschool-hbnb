"""Creates user"""
import re
import uuid
from datetime import datetime
from app import bcrypt

class User:
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.is_admin = kwargs.get('is_admin', False)

    def _validate(self):
        """Validates user information intake to be within requirements"""
        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("First name must be 1-50 characters")

        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("Last name must be 1-50 characters")

        if not self.email or not self.EMAIL_REGEX.match(self.email):
            raise ValueError("Invalid email format")

    def save(self):
        """Gets time were user made an update"""
        self.updated_at = datetime.now()

    def update(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def hash_password(self, password):
        """Hashes password to store after"""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Compares that password inputed matched hashed password"""
        return bcrypt.check_password_hash(self.password, password)
