"""
Custom Faker provider for Schema.org/Product properties.
Generates realistic data for products including e-commerce items.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgProductProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Product properties."""
    
    # Product-specific data
    PRODUCT_CATEGORIES = [
        "Electronics", "Clothing", "Books", "Home & Garden", "Toys",
        "Sports Equipment", "Jewelry", "Automotive", "Beauty Products",
        "Food & Beverages", "Office Supplies", "Pet Supplies", "Health",
        "Furniture", "Appliances", "Software", "Video Games", "Music",
        "Movies", "Tools", "Outdoor", "Baby Products", "Musical Instruments"
    ]
    
    BRANDS = [
        "TechCorp", "StyleBrand", "HomeGoods", "SportMax", "LuxuryLine",
        "EcoFriendly", "PremiumPlus", "ClassicBrand", "ModernStyle",
        "ProSeries", "EliteBrand", "StandardGoods", "ValueLine"
    ]
    
    CONDITIONS = [
        "NewCondition",
        "UsedCondition",
        "RefurbishedCondition",
        "DamagedCondition"
    ]
    
    def product_name(self):
        """Product name."""
        category = random.choice(self.PRODUCT_CATEGORIES)
        adjectives = self.fake.words(nb=2)
        nouns = self.fake.words(nb=1)
        return f"{' '.join(adjectives).title()} {nouns[0].title()} {category[:-1]}"
    
    def product_description(self):
        """Product description."""
        return self.common_description()
    
    def product_sku(self):
        """Stock Keeping Unit (SKU)."""
        prefix = random.choice(["SKU", "PROD", "ITEM"])
        number = random.randint(10000, 999999)
        return f"{prefix}-{number}"
    
    def product_gtin(self):
        """Global Trade Item Number (GTIN/UPC/EAN)."""
        # Generate 13-digit EAN-13 format
        return f"{random.randint(1000000000000, 9999999999999)}"
    
    def product_mpn(self):
        """Manufacturer Part Number."""
        prefix = random.choice(["MPN", "PN", "PART"])
        number = random.randint(1000, 99999)
        return f"{prefix}-{number}"
    
    def product_brand(self):
        """Brand name."""
        return random.choice(self.BRANDS)
    
    def product_manufacturer(self):
        """Manufacturer name."""
        return self.fake.company()
    
    def product_category(self):
        """Product category."""
        return random.choice(self.PRODUCT_CATEGORIES)
    
    def product_image_url(self):
        """Product image URL."""
        product_name = self.product_name().lower().replace(" ", "-")
        return f"https://example.com/images/products/{product_name}.jpg"
    
    def product_weight(self):
        """Product weight."""
        weight_kg = round(random.uniform(0.1, 50.0), 2)
        return f"{weight_kg} kg"
    
    def product_height(self):
        """Product height."""
        height_cm = round(random.uniform(5, 200), 1)
        return f"{height_cm} cm"
    
    def product_width(self):
        """Product width."""
        width_cm = round(random.uniform(5, 200), 1)
        return f"{width_cm} cm"
    
    def product_depth(self):
        """Product depth."""
        depth_cm = round(random.uniform(5, 200), 1)
        return f"{depth_cm} cm"
    
    def product_color(self):
        """Product color."""
        colors = ["Black", "White", "Red", "Blue", "Green", "Yellow", 
                 "Orange", "Purple", "Pink", "Gray", "Brown", "Silver", "Gold"]
        return random.choice(colors)
    
    def product_material(self):
        """Product material."""
        materials = ["Cotton", "Polyester", "Leather", "Plastic", "Metal",
                    "Wood", "Glass", "Ceramic", "Silk", "Wool", "Rubber"]
        return random.choice(materials)
    
    def product_condition(self):
        """Product condition."""
        return random.choice(self.CONDITIONS)
    
    def product_release_date(self):
        """Product release date."""
        return self.common_date(start_year=2010, end_year=2024)
    
    def product_model(self):
        """Product model number."""
        return f"Model-{random.randint(1000, 9999)}"
    
    def product_aggregate_rating(self):
        """Aggregate rating value (1-5 stars)."""
        return round(random.uniform(3.0, 5.0), 1)
    
    def product_review_count(self):
        """Number of reviews."""
        return random.randint(0, 500)


def create_product_data(num_entities=10, seed=None):
    """
    Generate product data using the custom provider.
    
    Args:
        num_entities: Number of product entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing product data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgProductProvider)
    
    products = []
    
    for i in range(num_entities):
        product = {
            "@type": "Product",
            "name": fake.product_name(),
            "description": fake.product_description(),
        }
        
        # Optional properties with varying probability
        if random.random() < 0.8:
            product["sku"] = fake.product_sku()
        
        if random.random() < 0.6:
            product["gtin"] = fake.product_gtin()
        
        if random.random() < 0.5:
            product["mpn"] = fake.product_mpn()
        
        if random.random() < 0.7:
            product["brand"] = fake.product_brand()
        
        if random.random() < 0.6:
            product["manufacturer"] = fake.product_manufacturer()
        
        product["category"] = fake.product_category()
        
        if random.random() < 0.8:
            product["image"] = fake.product_image_url()
        
        # Physical dimensions
        if random.random() < 0.5:
            product["weight"] = fake.product_weight()
        
        if random.random() < 0.4:
            product["height"] = fake.product_height()
            product["width"] = fake.product_width()
            product["depth"] = fake.product_depth()
        
        if random.random() < 0.6:
            product["color"] = fake.product_color()
        
        if random.random() < 0.4:
            product["material"] = fake.product_material()
        
        if random.random() < 0.7:
            product["itemCondition"] = fake.product_condition()
        
        if random.random() < 0.5:
            product["releaseDate"] = fake.product_release_date()
        
        if random.random() < 0.5:
            product["model"] = fake.product_model()
        
        # Ratings
        if random.random() < 0.6:
            rating = fake.product_aggregate_rating()
            review_count = fake.product_review_count()
            product["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        products.append(product)
    
    return products


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Product Provider\n")
    print("=" * 80)
    
    products = create_product_data(num_entities=3, seed=42)
    
    for i, product in enumerate(products, 1):
        print(f"\nProduct {i}:")
        print("-" * 80)
        for key, value in product.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

