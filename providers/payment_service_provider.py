"""
Custom Faker provider for Schema.org/PaymentService properties.
Generates realistic data for payment services.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
import random


class SchemaOrgPaymentServiceProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/PaymentService properties."""
    
    # PaymentService-specific data
    SERVICE_TYPES = [
        "Payment Processing", "Money Transfer", "Bill Payment",
        "Mobile Payment", "Online Payment", "Point of Sale",
        "Peer-to-Peer Payment", "Subscription Billing"
    ]
    
    SERVICE_PROVIDERS = [
        "PayPal", "Stripe", "Square", "Venmo", "Apple Pay",
        "Google Pay", "Zelle", "Western Union", "MoneyGram"
    ]
    
    PAYMENT_METHODS = [
        "Credit Card", "Debit Card", "Bank Transfer", "Digital Wallet",
        "Cryptocurrency", "ACH", "Wire Transfer", "Check"
    ]
    
    def payment_service_name(self):
        """Payment service name."""
        return random.choice(self.SERVICE_PROVIDERS)
    
    def payment_service_description(self):
        """Payment service description."""
        return self.common_description()
    
    def payment_service_service_type(self):
        """Type of payment service."""
        return random.choice(self.SERVICE_TYPES)
    
    def payment_service_provider(self):
        """Service provider."""
        return random.choice(self.SERVICE_PROVIDERS)
    
    def payment_service_payment_method(self):
        """Payment methods accepted."""
        num_methods = random.randint(2, 5)
        return random.sample(self.PAYMENT_METHODS, num_methods)
    
    def payment_service_area_served(self):
        """Geographic area served."""
        areas = [
            "Global", "North America", "Europe", "Asia Pacific",
            "United States", "Canada", "United Kingdom"
        ]
        return random.choice(areas)
    
    def payment_service_fees_and_commissions_specification(self):
        """Fees and commissions."""
        return {
            "transactionFee": round(random.uniform(0, 3.0), 2),
            "percentageFee": round(random.uniform(0, 5.0), 2),
            "monthlyFee": round(random.uniform(0, 30), 2)
        }
    
    def payment_service_url(self):
        """Service URL."""
        return self.common_url()
    
    def payment_service_telephone(self):
        """Service telephone."""
        return self.common_telephone()
    
    def payment_service_email(self):
        """Service email."""
        return self.common_email()
    
    def payment_service_currency(self):
        """Currencies supported."""
        currencies = ["USD", "EUR", "GBP", "CAD", "AUD", "JPY"]
        num_currencies = random.randint(1, 4)
        return random.sample(currencies, num_currencies)


def create_payment_service_data(num_entities=10, seed=None):
    """
    Generate payment service data using the custom provider.
    
    Args:
        num_entities: Number of payment service entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing payment service data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgPaymentServiceProvider)
    
    services = []
    
    for i in range(num_entities):
        service = {
            "@type": "PaymentService",
            "name": fake.payment_service_name(),
            "description": fake.payment_service_description(),
        }
        
        # Optional properties
        if random.random() < 0.8:
            service["serviceType"] = fake.payment_service_service_type()
        
        if random.random() < 0.9:
            service["provider"] = fake.payment_service_provider()
        
        if random.random() < 0.8:
            service["paymentMethod"] = fake.payment_service_payment_method()
        
        if random.random() < 0.7:
            service["areaServed"] = fake.payment_service_area_served()
        
        if random.random() < 0.6:
            service["feesAndCommissionsSpecification"] = fake.payment_service_fees_and_commissions_specification()
        
        if random.random() < 0.8:
            service["url"] = fake.payment_service_url()
        
        if random.random() < 0.6:
            service["telephone"] = fake.payment_service_telephone()
        
        if random.random() < 0.6:
            service["email"] = fake.payment_service_email()
        
        if random.random() < 0.7:
            service["currency"] = fake.payment_service_currency()
        
        services.append(service)
    
    return services


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org PaymentService Provider\n")
    print("=" * 80)
    
    services = create_payment_service_data(num_entities=3, seed=42)
    
    for i, service in enumerate(services, 1):
        print(f"\nPaymentService {i}:")
        print("-" * 80)
        for key, value in service.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            elif isinstance(value, list):
                print(f"  {key}: {', '.join(value)}")
            else:
                print(f"  {key}: {value}")

