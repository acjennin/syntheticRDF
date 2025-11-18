"""
Custom Faker provider for Schema.org/CurrencyConversionService properties.
Generates realistic data for currency conversion services.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
import random


class SchemaOrgCurrencyConversionServiceProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/CurrencyConversionService properties."""
    
    # CurrencyConversionService-specific data
    SERVICE_PROVIDERS = [
        "CurrencyExchange Pro", "Global Currency Services", "Forex Direct",
        "International Exchange", "Currency Hub", "Exchange Plus"
    ]
    
    CURRENCY_PAIRS = [
        ("USD", "EUR"), ("USD", "GBP"), ("USD", "JPY"), ("USD", "CAD"),
        ("EUR", "GBP"), ("EUR", "JPY"), ("GBP", "JPY"), ("USD", "AUD"),
        ("USD", "CHF"), ("EUR", "CHF")
    ]
    
    def currency_conversion_service_name(self):
        """Service name."""
        return random.choice(self.SERVICE_PROVIDERS)
    
    def currency_conversion_service_description(self):
        """Service description."""
        return self.common_description()
    
    def currency_conversion_service_provider(self):
        """Service provider."""
        return self.fake.company()
    
    def currency_conversion_service_area_served(self):
        """Geographic area served."""
        return random.choice(["Global", "North America", "Europe", "Asia Pacific"])
    
    def currency_conversion_service_exchange_rate(self):
        """Exchange rate."""
        return round(random.uniform(0.5, 2.0), 4)
    
    def currency_conversion_service_from_currency(self):
        """Source currency."""
        pair = random.choice(self.CURRENCY_PAIRS)
        return pair[0]
    
    def currency_conversion_service_to_currency(self):
        """Target currency."""
        pair = random.choice(self.CURRENCY_PAIRS)
        return pair[1]
    
    def currency_conversion_service_fee(self):
        """Service fee."""
        fees = [0, 2.50, 5.00, 7.50, 10.00, 15.00]
        return random.choice(fees)
    
    def currency_conversion_service_url(self):
        """Service URL."""
        return self.common_url()
    
    def currency_conversion_service_telephone(self):
        """Service telephone."""
        return self.common_telephone()


def create_currency_conversion_service_data(num_entities=10, seed=None):
    """
    Generate currency conversion service data using the custom provider.
    
    Args:
        num_entities: Number of service entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing currency conversion service data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgCurrencyConversionServiceProvider)
    
    services = []
    
    for i in range(num_entities):
        from_currency = fake.currency_conversion_service_from_currency()
        to_currency = fake.currency_conversion_service_to_currency()
        
        service = {
            "@type": "CurrencyConversionService",
            "name": fake.currency_conversion_service_name(),
            "description": fake.currency_conversion_service_description(),
            "fromCurrency": from_currency,
            "toCurrency": to_currency,
        }
        
        # Optional properties
        if random.random() < 0.8:
            service["provider"] = fake.currency_conversion_service_provider()
        
        if random.random() < 0.7:
            service["areaServed"] = fake.currency_conversion_service_area_served()
        
        if random.random() < 0.7:
            service["exchangeRate"] = fake.currency_conversion_service_exchange_rate()
        
        if random.random() < 0.6:
            service["fee"] = fake.currency_conversion_service_fee()
        
        if random.random() < 0.8:
            service["url"] = fake.currency_conversion_service_url()
        
        if random.random() < 0.6:
            service["telephone"] = fake.currency_conversion_service_telephone()
        
        services.append(service)
    
    return services


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org CurrencyConversionService Provider\n")
    print("=" * 80)
    
    services = create_currency_conversion_service_data(num_entities=3, seed=42)
    
    for i, service in enumerate(services, 1):
        print(f"\nCurrencyConversionService {i}:")
        print("-" * 80)
        for key, value in service.items():
            print(f"  {key}: {value}")

