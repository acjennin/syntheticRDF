"""
Custom Faker provider for Schema.org/Place properties.
Generates realistic data for places including locations, venues, and geographic entities.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
import random


class SchemaOrgPlaceProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Place properties."""
    
    # Place-specific data
    PLACE_TYPES = [
        "TouristAttraction", "LandmarksOrHistoricalBuildings", "Park",
        "Museum", "Restaurant", "Hotel", "Cafe", "Store", "Airport",
        "TrainStation", "BusStation", "Hospital", "School", "University"
    ]
    
    def place_name(self):
        """Place name."""
        place_types = [
            "Central", "Grand", "Main", "Historic", "Memorial",
            "National", "City", "Town", "Village", "Park"
        ]
        nouns = [
            "Square", "Plaza", "Park", "Museum", "Theater", "Center",
            "Hall", "Stadium", "Arena", "Library", "Gallery"
        ]
        return f"{random.choice(place_types)} {random.choice(nouns)}"
    
    def place_description(self):
        """Place description."""
        return self.common_description()
    
    def place_address(self):
        """Place address."""
        return self.common_address()
    
    def place_geo_latitude(self):
        """Geographic latitude."""
        return round(random.uniform(-90.0, 90.0), 6)
    
    def place_geo_longitude(self):
        """Geographic longitude."""
        return round(random.uniform(-180.0, 180.0), 6)
    
    def place_telephone(self):
        """Place telephone number."""
        return self.common_telephone()
    
    def place_url(self):
        """Place website URL."""
        return self.common_url()
    
    def place_image_url(self):
        """Place image URL."""
        place_name = self.place_name().lower().replace(" ", "-")
        return f"https://example.com/images/places/{place_name}.jpg"
    
    def place_photo_url(self):
        """Place photo URL."""
        return self.place_image_url()
    
    def place_opening_hours(self):
        """Opening hours specification."""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = random.choice(days)
        opens = f"{random.randint(6, 10):02d}:00"
        closes = f"{random.randint(17, 22):02d}:00"
        return {
            "dayOfWeek": day,
            "opens": opens,
            "closes": closes
        }
    
    def place_price_range(self):
        """Price range indicator."""
        ranges = ["$", "$$", "$$$", "$$$$"]
        return random.choice(ranges)
    
    def place_contained_in_place(self):
        """Larger place that contains this place."""
        return self.fake.city()
    
    def place_contains_place(self):
        """Smaller places contained within this place."""
        return self.fake.city()
    
    def place_has_map(self):
        """URL to a map of the place."""
        place_name = self.place_name().lower().replace(" ", "-")
        return f"https://maps.example.com/{place_name}"
    
    def place_maximum_attendee_capacity(self):
        """Maximum number of attendees."""
        capacities = [50, 100, 200, 500, 1000, 2000, 5000, 10000]
        return random.choice(capacities)
    
    def place_public_access(self):
        """Whether the place is publicly accessible."""
        return random.choice([True, False])


def create_place_data(num_entities=10, seed=None):
    """
    Generate place data using the custom provider.
    
    Args:
        num_entities: Number of place entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing place data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgPlaceProvider)
    
    places = []
    
    for i in range(num_entities):
        place = {
            "@type": "Place",
            "name": fake.place_name(),
            "description": fake.place_description(),
        }
        
        # Address
        if random.random() < 0.9:
            place["address"] = fake.place_address()
        
        # Geographic coordinates
        if random.random() < 0.8:
            place["geo"] = {
                "latitude": fake.place_geo_latitude(),
                "longitude": fake.place_geo_longitude()
            }
        
        # Contact information
        if random.random() < 0.7:
            place["telephone"] = fake.place_telephone()
        
        if random.random() < 0.6:
            place["url"] = fake.place_url()
        
        # Images
        if random.random() < 0.7:
            place["image"] = fake.place_image_url()
        
        if random.random() < 0.5:
            place["photo"] = fake.place_photo_url()
        
        # Opening hours
        if random.random() < 0.6:
            num_days = random.randint(1, 7)
            place["openingHoursSpecification"] = []
            for _ in range(num_days):
                place["openingHoursSpecification"].append(fake.place_opening_hours())
        
        # Price range (for venues)
        if random.random() < 0.4:
            place["priceRange"] = fake.place_price_range()
        
        # Containment relationships
        if random.random() < 0.3:
            place["containedInPlace"] = fake.place_contained_in_place()
        
        if random.random() < 0.2:
            place["containsPlace"] = fake.place_contains_place()
        
        # Map
        if random.random() < 0.5:
            place["hasMap"] = fake.place_has_map()
        
        # Capacity (for venues)
        if random.random() < 0.3:
            place["maximumAttendeeCapacity"] = fake.place_maximum_attendee_capacity()
        
        # Public access
        if random.random() < 0.5:
            place["publicAccess"] = fake.place_public_access()
        
        places.append(place)
    
    return places


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Place Provider\n")
    print("=" * 80)
    
    places = create_place_data(num_entities=3, seed=42)
    
    for i, place in enumerate(places, 1):
        print(f"\nPlace {i}:")
        print("-" * 80)
        for key, value in place.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            elif isinstance(value, list):
                print(f"  {key}:")
                for item in value:
                    if isinstance(item, dict):
                        print(f"    - {item}")
                    else:
                        print(f"    - {item}")
            else:
                print(f"  {key}: {value}")

