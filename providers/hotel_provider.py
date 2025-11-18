"""
Custom Faker provider for Schema.org/Hotel properties.
Generates realistic data for hotels and lodging businesses.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
import random


class SchemaOrgHotelProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Hotel properties."""
    
    # Hotel-specific data
    HOTEL_TYPES = [
        "Resort", "Boutique Hotel", "Business Hotel", "Luxury Hotel",
        "Budget Hotel", "Motel", "Inn", "Bed and Breakfast"
    ]
    
    AMENITIES = [
        "WiFi", "Swimming Pool", "Fitness Center", "Spa", "Restaurant",
        "Room Service", "Parking", "Pet Friendly", "Airport Shuttle",
        "Business Center", "Conference Rooms", "Bar", "Golf Course"
    ]
    
    def hotel_name(self):
        """Hotel name."""
        prefixes = ["Grand", "Royal", "Plaza", "Park", "Riverside", "Mountain View"]
        suffixes = ["Hotel", "Resort", "Inn", "Lodge", "Suites"]
        return f"{random.choice(prefixes)} {self.fake.city()} {random.choice(suffixes)}"
    
    def hotel_checkin_time(self):
        """Check-in time."""
        times = ["14:00", "15:00", "16:00", "14:30", "15:30"]
        return random.choice(times)
    
    def hotel_checkout_time(self):
        """Check-out time."""
        times = ["10:00", "11:00", "12:00", "10:30", "11:30"]
        return random.choice(times)
    
    def hotel_number_of_rooms(self):
        """Number of rooms."""
        # Realistic distribution
        ranges = [
            (10, 50, 0.3),      # Small: 30%
            (51, 150, 0.3),     # Medium: 30%
            (151, 300, 0.25),   # Large: 25%
            (301, 1000, 0.12),  # Very large: 12%
            (1001, 5000, 0.03)  # Resort: 3%
        ]
        
        rand = random.random()
        cumulative = 0
        for min_rooms, max_rooms, prob in ranges:
            cumulative += prob
            if rand <= cumulative:
                return random.randint(min_rooms, max_rooms)
        
        return random.randint(50, 200)
    
    def hotel_pets_allowed(self):
        """Whether pets are allowed."""
        return random.choice([True, False])
    
    def hotel_star_rating(self):
        """Star rating (1-5 stars)."""
        # Weighted towards 3-4 stars
        weights = [0.05, 0.10, 0.25, 0.40, 0.20]  # 1-5 stars
        ratings = [1, 2, 3, 4, 5]
        return random.choices(ratings, weights=weights)[0]
    
    def hotel_amenity_feature(self):
        """Hotel amenities."""
        num_amenities = random.randint(3, 8)
        return random.sample(self.AMENITIES, num_amenities)
    
    def hotel_price_range(self):
        """Price range."""
        ranges = ["$", "$$", "$$$", "$$$$"]
        return random.choice(ranges)
    
    def hotel_aggregate_rating(self):
        """Hotel aggregate rating."""
        return round(random.uniform(3.0, 5.0), 1)
    
    def hotel_review_count(self):
        """Number of hotel reviews."""
        return random.randint(20, 1000)
    
    def hotel_geo_latitude(self):
        """Geographic latitude."""
        return round(random.uniform(-90.0, 90.0), 6)
    
    def hotel_geo_longitude(self):
        """Geographic longitude."""
        return round(random.uniform(-180.0, 180.0), 6)


def create_hotel_data(num_entities=10, seed=None):
    """
    Generate hotel data using the custom provider.
    
    Args:
        num_entities: Number of hotel entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing hotel data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgHotelProvider)
    
    hotels = []
    
    for i in range(num_entities):
        hotel = {
            "@type": "Hotel",
            "name": fake.hotel_name(),
            "description": fake.common_description(),
        }
        
        # Inherited LocalBusiness/Organization properties
        hotel["legalName"] = fake.common_legal_name()
        hotel["email"] = fake.common_email()
        hotel["telephone"] = fake.common_telephone()
        hotel["url"] = fake.common_url()
        
        if random.random() < 0.9:
            hotel["address"] = fake.common_address()
        
        # Hotel-specific properties
        hotel["checkinTime"] = fake.hotel_checkin_time()
        hotel["checkoutTime"] = fake.hotel_checkout_time()
        hotel["numberOfRooms"] = fake.hotel_number_of_rooms()
        hotel["petsAllowed"] = fake.hotel_pets_allowed()
        
        if random.random() < 0.8:
            hotel["starRating"] = {
                "ratingValue": fake.hotel_star_rating(),
                "bestRating": 5,
                "worstRating": 1
            }
        
        if random.random() < 0.8:
            amenities = fake.hotel_amenity_feature()
            hotel["amenityFeature"] = [{"name": amenity} for amenity in amenities]
        
        if random.random() < 0.7:
            hotel["priceRange"] = fake.hotel_price_range()
        
        # Geographic location
        if random.random() < 0.9:
            hotel["geo"] = {
                "latitude": fake.hotel_geo_latitude(),
                "longitude": fake.hotel_geo_longitude()
            }
        
        # Ratings
        if random.random() < 0.7:
            rating = fake.hotel_aggregate_rating()
            review_count = fake.hotel_review_count()
            hotel["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        hotels.append(hotel)
    
    return hotels


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Hotel Provider\n")
    print("=" * 80)
    
    hotels = create_hotel_data(num_entities=3, seed=42)
    
    for i, hotel in enumerate(hotels, 1):
        print(f"\nHotel {i}:")
        print("-" * 80)
        for key, value in hotel.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    if isinstance(v, list):
                        print(f"    {k}:")
                        for item in v:
                            if isinstance(item, dict):
                                print(f"      - {item}")
                            else:
                                print(f"      - {item}")
                    else:
                        print(f"    {k}: {v}")
            elif isinstance(value, list):
                print(f"  {key}:")
                for item in value:
                    print(f"    - {item}")
            else:
                print(f"  {key}: {value}")

