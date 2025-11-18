"""
Custom Faker provider for Schema.org/Offer properties.
Generates realistic data for product/service offers linking Products to Organizations.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgOfferProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Offer properties."""
    
    # Offer-specific data
    AVAILABILITIES = [
        "InStock",
        "OutOfStock",
        "PreOrder",
        "LimitedAvailability",
        "OnlineOnly",
        "InStoreOnly"
    ]
    
    ITEM_CONDITIONS = [
        "NewCondition",
        "UsedCondition",
        "RefurbishedCondition",
        "DamagedCondition"
    ]
    
    def offer_price(self):
        """Offer price."""
        return self.common_price(min_value=5, max_value=2000)
    
    def offer_price_currency(self):
        """Price currency."""
        return self.common_currency_code()
    
    def offer_price_valid_until(self):
        """Date until which the price is valid."""
        future_date = datetime.now() + timedelta(days=random.randint(1, 365))
        return future_date.isoformat()
    
    def offer_availability(self):
        """Item availability."""
        return random.choice(self.AVAILABILITIES)
    
    def offer_item_condition(self):
        """Condition of the item."""
        return random.choice(self.ITEM_CONDITIONS)
    
    def offer_seller(self):
        """Seller organization name."""
        return self.fake.company()
    
    def offer_url(self):
        """URL to the offer."""
        return self.common_url()
    
    def offer_valid_from(self):
        """Date from which the offer is valid."""
        past_date = datetime.now() - timedelta(days=random.randint(0, 30))
        return past_date.isoformat()
    
    def offer_valid_through(self):
        """Date until which the offer is valid."""
        future_date = datetime.now() + timedelta(days=random.randint(1, 365))
        return future_date.isoformat()
    
    def offer_eligible_region(self):
        """Region where the offer is valid."""
        return self.fake.country()
    
    def offer_price_specification(self, base_price=None):
        """Price specification with unit pricing."""
        if base_price is None:
            base_price = self.offer_price()
        
        return {
            "price": base_price,
            "priceCurrency": self.offer_price_currency(),
            "valueAddedTaxIncluded": random.choice([True, False])
        }
    
    def offer_shipping_details(self):
        """Shipping details."""
        return {
            "shippingRate": {
                "value": round(random.uniform(0, 25), 2),
                "currency": self.offer_price_currency()
            },
            "shippingDestination": {
                "addressCountry": self.fake.country_code()
            },
            "deliveryTime": {
                "minValue": random.randint(1, 3),
                "maxValue": random.randint(4, 14),
                "unitCode": "DAY"
            }
        }
    
    def offer_warranty(self):
        """Warranty information."""
        return {
            "warrantyScope": random.choice(["ManufacturerWarranty", "ExtendedWarranty"]),
            "durationOfWarranty": f"P{random.randint(1, 5)}Y"
        }


def create_offer_data(num_entities=10, seed=None):
    """
    Generate offer data using the custom provider.
    
    Args:
        num_entities: Number of offer entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing offer data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgOfferProvider)
    
    offers = []
    
    for i in range(num_entities):
        price = fake.offer_price()
        
        offer = {
            "@type": "Offer",
            "price": price,
            "priceCurrency": fake.offer_price_currency(),
            "availability": fake.offer_availability(),
        }
        
        # Optional properties
        if random.random() < 0.7:
            offer["priceValidUntil"] = fake.offer_price_valid_until()
        
        if random.random() < 0.8:
            offer["itemCondition"] = fake.offer_item_condition()
        
        if random.random() < 0.9:
            offer["seller"] = fake.offer_seller()
        
        if random.random() < 0.8:
            offer["url"] = fake.offer_url()
        
        if random.random() < 0.6:
            offer["validFrom"] = fake.offer_valid_from()
        
        if random.random() < 0.7:
            offer["validThrough"] = fake.offer_valid_through()
        
        if random.random() < 0.5:
            offer["eligibleRegion"] = fake.offer_eligible_region()
        
        if random.random() < 0.4:
            offer["priceSpecification"] = fake.offer_price_specification(price)
        
        if random.random() < 0.3:
            offer["shippingDetails"] = fake.offer_shipping_details()
        
        if random.random() < 0.3:
            offer["warranty"] = fake.offer_warranty()
        
        offers.append(offer)
    
    return offers


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Offer Provider\n")
    print("=" * 80)
    
    offers = create_offer_data(num_entities=3, seed=42)
    
    for i, offer in enumerate(offers, 1):
        print(f"\nOffer {i}:")
        print("-" * 80)
        for key, value in offer.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    if isinstance(v, dict):
                        print(f"    {k}:")
                        for k2, v2 in v.items():
                            print(f"      {k2}: {v2}")
                    else:
                        print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

