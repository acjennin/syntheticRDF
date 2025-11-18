"""
Custom Faker provider for Schema.org/PaymentCard properties.
Generates realistic data for payment cards (base class for credit/debit cards).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgPaymentCardProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/PaymentCard properties."""
    
    # PaymentCard-specific data
    CARD_TYPES = [
        "Credit Card", "Debit Card", "Prepaid Card", "Gift Card"
    ]
    
    CARD_NETWORKS = [
        "Visa", "Mastercard", "American Express", "Discover",
        "JCB", "UnionPay", "Diners Club"
    ]
    
    def payment_card_name(self):
        """Payment card name."""
        return random.choice(self.CARD_TYPES)
    
    def payment_card_description(self):
        """Payment card description."""
        return self.common_description()
    
    def payment_card_card_number(self):
        """Card number (masked)."""
        last_four = random.randint(1000, 9999)
        return f"**** **** **** {last_four}"
    
    def payment_card_card_holder_name(self):
        """Cardholder name."""
        return self.fake.name()
    
    def payment_card_expires(self):
        """Card expiration date."""
        future_date = datetime.now() + timedelta(days=random.randint(365, 1825))
        return future_date.strftime("%Y-%m")
    
    def payment_card_currency(self):
        """Currency."""
        return self.common_currency_code()
    
    def payment_card_issuer(self):
        """Card issuer."""
        issuers = [
            "Chase", "Bank of America", "Wells Fargo", "Citibank",
            "Capital One", "Discover", "American Express", "US Bank"
        ]
        return random.choice(issuers)
    
    def payment_card_network(self):
        """Card network."""
        return random.choice(self.CARD_NETWORKS)
    
    def payment_card_date_issued(self):
        """Date card was issued."""
        return self.common_date(start_year=2015, end_year=2024)
    
    def payment_card_contactless_payment(self):
        """Whether card supports contactless payment."""
        return random.choice([True, False])


def create_payment_card_data(num_entities=10, seed=None):
    """
    Generate payment card data using the custom provider.
    
    Args:
        num_entities: Number of payment card entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing payment card data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgPaymentCardProvider)
    
    cards = []
    
    for i in range(num_entities):
        card = {
            "@type": "PaymentCard",
            "name": fake.payment_card_name(),
            "description": fake.payment_card_description(),
        }
        
        # Optional properties
        if random.random() < 0.8:
            card["cardNumber"] = fake.payment_card_card_number()
        
        if random.random() < 0.8:
            card["cardHolderName"] = fake.payment_card_card_holder_name()
        
        if random.random() < 0.7:
            card["expires"] = fake.payment_card_expires()
        
        if random.random() < 0.8:
            card["currency"] = fake.payment_card_currency()
        
        if random.random() < 0.7:
            card["issuer"] = fake.payment_card_issuer()
        
        if random.random() < 0.7:
            card["network"] = fake.payment_card_network()
        
        if random.random() < 0.6:
            card["dateIssued"] = fake.payment_card_date_issued()
        
        if random.random() < 0.5:
            card["contactlessPayment"] = fake.payment_card_contactless_payment()
        
        cards.append(card)
    
    return cards


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org PaymentCard Provider\n")
    print("=" * 80)
    
    cards = create_payment_card_data(num_entities=3, seed=42)
    
    for i, card in enumerate(cards, 1):
        print(f"\nPaymentCard {i}:")
        print("-" * 80)
        for key, value in card.items():
            print(f"  {key}: {value}")

