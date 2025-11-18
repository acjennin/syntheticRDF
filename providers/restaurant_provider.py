"""
Custom Faker provider for Schema.org/Restaurant properties.
Generates realistic data for restaurants (specialization of LocalBusiness).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
import random


class SchemaOrgRestaurantProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Restaurant properties."""
    
    # Restaurant-specific data
    CUISINES = [
        "Italian", "Chinese", "Japanese", "Mexican", "Indian",
        "French", "Thai", "American", "Mediterranean", "Greek",
        "Korean", "Vietnamese", "Spanish", "German", "Brazilian"
    ]
    
    PRICE_RANGES = ["$", "$$", "$$$", "$$$$"]
    
    def restaurant_name(self):
        """Restaurant name."""
        return self.fake.company() + " " + random.choice(["Restaurant", "Bistro", "Cafe", "Grill", "Kitchen"])
    
    def restaurant_serves_cuisine(self):
        """Type of cuisine served."""
        return random.choice(self.CUISINES)
    
    def restaurant_menu_url(self):
        """URL to the restaurant menu."""
        restaurant_name = self.restaurant_name().lower().replace(" ", "-")
        return f"https://example.com/menus/{restaurant_name}"
    
    def restaurant_accepts_reservations(self):
        """Whether restaurant accepts reservations."""
        return random.choice([True, False])
    
    def restaurant_has_menu(self):
        """Whether restaurant has a menu."""
        return True  # Most restaurants have menus
    
    def restaurant_price_range(self):
        """Price range."""
        return random.choice(self.PRICE_RANGES)
    
    def restaurant_aggregate_rating(self):
        """Restaurant aggregate rating."""
        return round(random.uniform(3.0, 5.0), 1)
    
    def restaurant_review_count(self):
        """Number of restaurant reviews."""
        return random.randint(10, 500)
    
    def restaurant_opening_hours(self):
        """Restaurant opening hours."""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = random.choice(days)
        # Restaurants typically open later and close later
        opens = f"{random.randint(10, 12):02d}:00"
        closes = f"{random.randint(20, 23):02d}:00"
        return {
            "dayOfWeek": day,
            "opens": opens,
            "closes": closes
        }
    
    def restaurant_geo_latitude(self):
        """Geographic latitude."""
        return round(random.uniform(-90.0, 90.0), 6)
    
    def restaurant_geo_longitude(self):
        """Geographic longitude."""
        return round(random.uniform(-180.0, 180.0), 6)
    
    def restaurant_payment_accepted(self):
        """Payment methods accepted."""
        methods = ["Cash", "Credit Card", "Debit Card", "Mobile Payment"]
        num_methods = random.randint(2, 4)
        return random.sample(methods, num_methods)


def create_restaurant_data(num_entities=10, seed=None):
    """
    Generate restaurant data using the custom provider.
    
    Args:
        num_entities: Number of restaurant entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing restaurant data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgRestaurantProvider)
    
    restaurants = []
    
    for i in range(num_entities):
        restaurant = {
            "@type": "Restaurant",
            "name": fake.restaurant_name(),
            "description": fake.common_description(),
        }
        
        # Inherited LocalBusiness/Organization properties
        restaurant["legalName"] = fake.common_legal_name()
        restaurant["email"] = fake.common_email()
        restaurant["telephone"] = fake.common_telephone()
        restaurant["url"] = fake.common_url()
        
        if random.random() < 0.9:
            restaurant["address"] = fake.common_address()
        
        # Restaurant-specific properties
        restaurant["servesCuisine"] = fake.restaurant_serves_cuisine()
        
        if random.random() < 0.7:
            restaurant["menu"] = fake.restaurant_menu_url()
        
        restaurant["acceptsReservations"] = fake.restaurant_accepts_reservations()
        restaurant["hasMenu"] = fake.restaurant_has_menu()
        
        if random.random() < 0.8:
            restaurant["priceRange"] = fake.restaurant_price_range()
        
        # Opening hours
        if random.random() < 0.9:
            num_days = random.randint(5, 7)
            restaurant["openingHoursSpecification"] = []
            for _ in range(num_days):
                restaurant["openingHoursSpecification"].append(fake.restaurant_opening_hours())
        
        # Geographic location
        if random.random() < 0.8:
            restaurant["geo"] = {
                "latitude": fake.restaurant_geo_latitude(),
                "longitude": fake.restaurant_geo_longitude()
            }
        
        # Payment
        if random.random() < 0.8:
            restaurant["paymentAccepted"] = fake.restaurant_payment_accepted()
        
        # Ratings
        if random.random() < 0.7:
            rating = fake.restaurant_aggregate_rating()
            review_count = fake.restaurant_review_count()
            restaurant["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        restaurants.append(restaurant)
    
    return restaurants


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Restaurant Provider\n")
    print("=" * 80)
    
    restaurants = create_restaurant_data(num_entities=3, seed=42)
    
    for i, restaurant in enumerate(restaurants, 1):
        print(f"\nRestaurant {i}:")
        print("-" * 80)
        for key, value in restaurant.items():
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

