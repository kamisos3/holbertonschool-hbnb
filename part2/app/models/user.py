#!/usr/bin/python3
"""Creates user"""

import re
import uuid
from datetime import datetime

class User:
        EMAIL_REGEX = re.compile(r'^[\w\.-]+\.\w+$')

    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self._validate()

def _validate(self):
    if not self.first_name or len(self.first_name) > 50:
        raise ValueError("First name must be 1-50 characters")

    if not self.last_name or len(self.last_name) > 50:
        raise ValueError("Last name must be 1-50 characters")

    if not self.email or not self.EMAIL_REGEX.match(self.email):
        raise ValueError("Invalid email format")

def save(self):
    self.updated_at = datetime.now()

def update(self, data: dict):
    for key, value in data.items():
        if key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            self.save()
            self._validate()
