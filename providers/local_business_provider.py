"""
Custom Faker provider for Schema.org/LocalBusiness properties.
Generates realistic data for local businesses (specialization of Organization).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
import random


class SchemaOrgLocalBusinessProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/LocalBusiness properties."""
    
    # LocalBusiness-specific data
    BUSINESS_TYPES = [
        "Restaurant", "Store", "AutomotiveBusiness", "ChildCare",
        "DryCleaningOrLaundry", "EmergencyService", "EntertainmentBusiness",
        "FinancialService", "FoodEstablishment", "GovernmentOffice",
        "HealthAndBeautyBusiness", "HomeAndConstructionBusiness",
        "InternetCafe", "LegalService", "Library", "LodgingBusiness",
        "MedicalBusiness", "ProfessionalService", "RealEstateAgent",
        "RecyclingCenter", "SelfStorage", "ShoppingCenter", "SportsActivityLocation",
        "Store", "TattooParlor", "TravelAgency", "VeterinaryCare"
    ]
    
    PAYMENT_METHODS = [
        "Cash", "Credit Card", "Debit Card", "Check", "Mobile Payment",
        "Cryptocurrency", "Gift Card", "Bank Transfer"
    ]
    
    CURRENCIES_ACCEPTED = [
        "USD", "EUR", "GBP", "CAD", "AUD"
    ]
    
    INDUSTRIES = [
        "Technology", "Healthcare", "Finance", "Education", "Manufacturing",
        "Retail", "Hospitality", "Transportation", "Energy", "Telecommunications",
        "Real Estate", "Media", "Entertainment", "Agriculture", "Construction",
        "Legal Services", "Consulting", "Pharmaceuticals", "Biotechnology",
        "Aerospace", "Automotive", "Insurance", "Banking"
    ]
    
    def local_business_name(self):
        """Local business name."""
        return self.fake.company()
    
    def local_business_price_range(self):
        """Price range indicator."""
        ranges = ["$", "$$", "$$$", "$$$$"]
        return random.choice(ranges)
    
    def local_business_payment_accepted(self):
        """Payment methods accepted."""
        num_methods = random.randint(2, 5)
        return random.sample(self.PAYMENT_METHODS, num_methods)
    
    def local_business_currencies_accepted(self):
        """Currencies accepted."""
        num_currencies = random.randint(1, 3)
        return random.sample(self.CURRENCIES_ACCEPTED, num_currencies)
    
    def local_business_opening_hours(self):
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
    
    def local_business_geo_latitude(self):
        """Geographic latitude."""
        return round(random.uniform(-90.0, 90.0), 6)
    
    def local_business_geo_longitude(self):
        """Geographic longitude."""
        return round(random.uniform(-180.0, 180.0), 6)
    
    def local_business_area_served(self):
        """Geographic area served."""
        areas = [
            "Local", "Regional", "National", "International",
            self.fake.city(), self.fake.state(), self.fake.country()
        ]
        return random.choice(areas)
    
    def local_business_has_map(self):
        """URL to a map of the business."""
        business_name = self.local_business_name().lower().replace(" ", "-")
        return f"https://maps.example.com/{business_name}"
    
    def local_business_aggregate_rating(self):
        """Aggregate rating value."""
        return round(random.uniform(3.0, 5.0), 1)
    
    def local_business_review_count(self):
        """Number of reviews."""
        return random.randint(5, 200)


def create_local_business_data(num_entities=10, seed=None):
    """
    Generate local business data using the custom provider.
    
    Args:
        num_entities: Number of local business entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing local business data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgLocalBusinessProvider)
    
    businesses = []
    
    for i in range(num_entities):
        business = {
            "@type": "LocalBusiness",
            "name": fake.local_business_name(),
            "description": fake.common_description(),
        }
        
        # Inherited Organization properties
        business["legalName"] = fake.common_legal_name()
        business["email"] = fake.common_email()
        business["telephone"] = fake.common_telephone()
        business["url"] = fake.common_url()
        
        if random.random() < 0.8:
            business["address"] = fake.common_address()
        
        # LocalBusiness-specific properties
        if random.random() < 0.7:
            business["priceRange"] = fake.local_business_price_range()
        
        if random.random() < 0.8:
            business["paymentAccepted"] = fake.local_business_payment_accepted()
        
        if random.random() < 0.6:
            business["currenciesAccepted"] = fake.local_business_currencies_accepted()
        
        if random.random() < 0.9:
            num_days = random.randint(5, 7)
            business["openingHoursSpecification"] = []
            for _ in range(num_days):
                business["openingHoursSpecification"].append(fake.local_business_opening_hours())
        
        # Geographic location
        if random.random() < 0.8:
            business["geo"] = {
                "latitude": fake.local_business_geo_latitude(),
                "longitude": fake.local_business_geo_longitude()
            }
        
        if random.random() < 0.6:
            business["areaServed"] = fake.local_business_area_served()
        
        if random.random() < 0.5:
            business["hasMap"] = fake.local_business_has_map()
        
        # Ratings
        if random.random() < 0.6:
            rating = fake.local_business_aggregate_rating()
            review_count = fake.local_business_review_count()
            business["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        # Industry/type
        if random.random() < 0.7:
            business["industry"] = random.choice(SchemaOrgLocalBusinessProvider.INDUSTRIES)
        
        businesses.append(business)
    
    return businesses


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org LocalBusiness Provider\n")
    print("=" * 80)
    
    businesses = create_local_business_data(num_entities=3, seed=42)
    
    for i, business in enumerate(businesses, 1):
        print(f"\nLocalBusiness {i}:")
        print("-" * 80)
        for key, value in business.items():
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

