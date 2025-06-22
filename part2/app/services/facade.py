"""This class handles communication within the 3 arquitecture layers"""
from app.models.user import User
from app.persistance.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_place(self, place_data):
        price = place_data.get("price")
        latitude = place_data.get("latitude")
        longitude = place_data.get("longitude")

        if price < 0 or not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid price, latitude or longitude")

        owner = self.user_repo.get(place_data["owner_id"])
        if not owner:
            raise ValueError("Owner not found")

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return "not_found"

        try:
            for key, value in place_data.items():
                setattr(place, key, value)
            self.place_repo.update(place_id, place_data)
            return place
        except ValueError:
            return "invalid_data"

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, update_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        try:
            amenity.update(update_data)
            self.amenity_repo.update(amenity_id, update_data)
            return amenity
        except ValueError as e:
            return str(e)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, updateid, update_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None

        original_email = user.email

        user.update(update_data)

        if 'email' in update_data and update_data['email'] != original_email:
            existing_user = self.get_user_by_email(update_data['email'])
            if existing_user and existing_user.id != user_id:
                return 'email_exists'

        self.user_repo.update(user_id, update_data)
        return user
