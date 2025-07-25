#!/bin/usr/python3
"""Created a place with service details"""

import uuid
from datetime import datetime
from typing import List

class Place:
    def __init__(self, title: str, description: str, price: float, latitude: float,
                 longitude: float, owner: 'User'):
    self.id = str(uuid.uuid4())
    self.title = title
    self.description = description
    self.price = price
    self.latitude = latitude
    self.longitude = longitude
    self.owner = owner
    self.reviews: List['Review'] = []
    self.amenities: List['Amenity'] = []
    self.created_at = datetime.now()
    self.updated_at = self.created_at
    self._validate()

def _validate(self):
    if not self.title or len(self.title) > 100:
        raise ValueError("Title must be 1-100 characters")

    if self.price <= 0:
        raise ValueError("Price must be positive")

    if not (-90.0 <= self.latitude <= 90.0):
        raise ValueError("Latitude must be between -90.0 and 90.0")

    if not (-180.0 <= self.longitude <= 180.0):
        raise ValueError("Longitude must be between -180.0 and 180.0")

def add_review(self, review: 'Review'):
    if review.place != self:
        raise ValueError("Review does not belong to this place")

def add_amenity(self, amenity: 'Amenity'):
    if amenity not in self.amenities:
        self.amenities.append(amenity)

def save(self):
    self.updated_at = datetime.now()

def update(self, data: dict):
    for key, value in data.items():
        if hasattr(self, key):
            setattr(self, key, value)
    self.save()
    self._validate()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        self._price = value

    @property
    def latitude(self, value):
        return self.latitude

    @latitude.setter
    def latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValueError("latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = value

    def to_dict(self, full=False):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'amenities': self.amenities
        }
        return data
