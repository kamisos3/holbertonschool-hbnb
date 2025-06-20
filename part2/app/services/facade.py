#!/usr/bin/python3
"""This class handles communication within the 3 arquitecture layers"""

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        pass

    def get_place(self, place_id):
        # Implementing more logic later
        pass
