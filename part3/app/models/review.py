#!/usr/bin/python3
"""Allows to write review"""
import uuid
from datetime import datetime

class Review:
    def __init__(self, text: str, rating: int, place: 'Place', user: 'User'):
        self.id = str(uuid.uuid4())
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self._validate()

    def _validate(self):
        if not self.text:
            raise ValueError("Review text is required")

        if not 1 <= self.rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

    def save(self):
        self.updated_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place.id,
            'user_id': self.user.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }