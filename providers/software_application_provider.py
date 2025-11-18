"""
Custom Faker provider for Schema.org/SoftwareApplication properties.
Generates realistic data for software applications and apps.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgSoftwareApplicationProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/SoftwareApplication properties."""
    
    # SoftwareApplication-specific data
    APPLICATION_CATEGORIES = [
        "Game", "BusinessApplication", "SocialNetworkingApplication",
        "TravelApplication", "ShoppingApplication", "SportsApplication",
        "LifestyleApplication", "BusinessApplication", "DesignApplication",
        "DeveloperApplication", "DriverApplication", "EducationalApplication",
        "HealthApplication", "FinanceApplication", "FoodApplication",
        "NewsApplication", "PhotographyApplication", "ProductivityApplication"
    ]
    
    OPERATING_SYSTEMS = [
        "Android", "iOS", "Windows", "macOS", "Linux", "Web Browser",
        "Windows Phone", "BlackBerry", "Chrome OS"
    ]
    
    def software_application_name(self):
        """Application name."""
        prefixes = ["Smart", "Pro", "Ultra", "Quick", "Easy", "Power"]
        nouns = ["App", "Tool", "Manager", "Assistant", "Helper", "Studio"]
        return f"{random.choice(prefixes)}{random.choice(nouns)}"
    
    def software_application_description(self):
        """Application description."""
        return self.common_description()
    
    def software_application_application_category(self):
        """Application category."""
        return random.choice(self.APPLICATION_CATEGORIES)
    
    def software_application_operating_system(self):
        """Operating system required."""
        return random.choice(self.OPERATING_SYSTEMS)
    
    def software_application_software_version(self):
        """Software version."""
        major = random.randint(1, 10)
        minor = random.randint(0, 9)
        patch = random.randint(0, 99)
        return f"{major}.{minor}.{patch}"
    
    def software_application_offers_price(self):
        """Application price."""
        # Many apps are free, some are paid
        if random.random() < 0.6:
            return 0
        return self.common_price(min_value=0.99, max_value=99.99)
    
    def software_application_offers_currency(self):
        """Price currency."""
        return self.common_currency_code()
    
    def software_application_aggregate_rating(self):
        """Application aggregate rating."""
        return round(random.uniform(3.0, 5.0), 1)
    
    def software_application_review_count(self):
        """Number of application reviews."""
        return random.randint(10, 10000)
    
    def software_application_download_url(self):
        """URL to download the application."""
        app_name = self.software_application_name().lower().replace(" ", "-")
        return f"https://example.com/downloads/{app_name}"
    
    def software_application_screenshot_url(self):
        """Application screenshot URL."""
        app_name = self.software_application_name().lower().replace(" ", "-")
        return f"https://example.com/screenshots/{app_name}-1.jpg"
    
    def software_application_author(self):
        """Application author/developer."""
        return self.fake.company()
    
    def software_application_publisher(self):
        """Application publisher."""
        return self.fake.company()
    
    def software_application_release_notes(self):
        """Release notes."""
        notes = [
            "Bug fixes and performance improvements",
            "New features and enhanced functionality",
            "Updated UI and improved user experience",
            "Security updates and stability improvements"
        ]
        return random.choice(notes)
    
    def software_application_file_size(self):
        """Application file size."""
        sizes_mb = [5, 10, 25, 50, 100, 250, 500, 1000]
        size = random.choice(sizes_mb)
        return f"{size} MB"
    
    def software_application_date_published(self):
        """Date application was published."""
        return self.common_date(start_year=2015, end_year=2024)
    
    def software_application_date_modified(self):
        """Date application was last modified."""
        return self.common_date(start_year=2020, end_year=2024)


def create_software_application_data(num_entities=10, seed=None):
    """
    Generate software application data using the custom provider.
    
    Args:
        num_entities: Number of software application entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing software application data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgSoftwareApplicationProvider)
    
    applications = []
    
    for i in range(num_entities):
        price = fake.software_application_offers_price()
        
        application = {
            "@type": "SoftwareApplication",
            "name": fake.software_application_name(),
            "description": fake.software_application_description(),
            "applicationCategory": fake.software_application_application_category(),
        }
        
        # Optional properties
        if random.random() < 0.9:
            application["operatingSystem"] = fake.software_application_operating_system()
        
        if random.random() < 0.8:
            application["softwareVersion"] = fake.software_application_software_version()
        
        # Offers (price)
        if random.random() < 0.9:
            application["offers"] = {
                "price": price,
                "priceCurrency": fake.software_application_offers_currency()
            }
        
        # Ratings
        if random.random() < 0.7:
            rating = fake.software_application_aggregate_rating()
            review_count = fake.software_application_review_count()
            application["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        if random.random() < 0.7:
            application["downloadUrl"] = fake.software_application_download_url()
        
        if random.random() < 0.6:
            application["screenshot"] = fake.software_application_screenshot_url()
        
        if random.random() < 0.8:
            application["author"] = fake.software_application_author()
        
        if random.random() < 0.7:
            application["publisher"] = fake.software_application_publisher()
        
        if random.random() < 0.5:
            application["releaseNotes"] = fake.software_application_release_notes()
        
        if random.random() < 0.6:
            application["fileSize"] = fake.software_application_file_size()
        
        if random.random() < 0.7:
            application["datePublished"] = fake.software_application_date_published()
        
        if random.random() < 0.6:
            application["dateModified"] = fake.software_application_date_modified()
        
        applications.append(application)
    
    return applications


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org SoftwareApplication Provider\n")
    print("=" * 80)
    
    applications = create_software_application_data(num_entities=3, seed=42)
    
    for i, application in enumerate(applications, 1):
        print(f"\nSoftwareApplication {i}:")
        print("-" * 80)
        for key, value in application.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

