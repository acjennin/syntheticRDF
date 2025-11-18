"""
Custom Faker provider for Schema.org/CreditCard properties.
Generates realistic data for credit cards (specialization of PaymentCard/LoanOrCredit).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgCreditCardProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/CreditCard properties."""
    
    # CreditCard-specific data
    CARD_ISSUERS = [
        "Visa", "Mastercard", "American Express", "Discover",
        "Chase", "Bank of America", "Capital One", "Citi", "Wells Fargo"
    ]
    
    CARD_TYPES = [
        "Rewards", "Cash Back", "Travel", "Business", "Student",
        "Secured", "Balance Transfer", "Low Interest"
    ]
    
    def credit_card_name(self):
        """Credit card name."""
        issuer = random.choice(self.CARD_ISSUERS)
        card_type = random.choice(self.CARD_TYPES)
        return f"{issuer} {card_type} Card"
    
    def credit_card_description(self):
        """Credit card description."""
        return self.common_description()
    
    def credit_card_card_number(self):
        """Credit card number (masked for security)."""
        # Generate last 4 digits
        last_four = random.randint(1000, 9999)
        return f"**** **** **** {last_four}"
    
    def credit_card_issuer(self):
        """Card issuer."""
        return random.choice(self.CARD_ISSUERS)
    
    def credit_card_annual_percentage_rate(self):
        """Annual Percentage Rate (APR)."""
        return round(random.uniform(12.0, 30.0), 2)
    
    def credit_card_credit_limit(self):
        """Credit limit."""
        limits = [
            (500, 2000, 0.2),
            (2000, 5000, 0.3),
            (5000, 10000, 0.25),
            (10000, 25000, 0.15),
            (25000, 100000, 0.1)
        ]
        
        rand = random.random()
        cumulative = 0
        for min_limit, max_limit, prob in limits:
            cumulative += prob
            if rand <= cumulative:
                return round(random.uniform(min_limit, max_limit), 2)
        
        return round(random.uniform(500, 5000), 2)
    
    def credit_card_currency(self):
        """Currency."""
        return self.common_currency_code()
    
    def credit_card_interest_rate(self):
        """Interest rate."""
        return round(random.uniform(10.0, 28.0), 2)
    
    def credit_card_annual_fee(self):
        """Annual fee."""
        fees = [0, 0, 0, 25, 50, 95, 150, 250, 450, 550]  # Many cards have no fee
        return random.choice(fees)
    
    def credit_card_cashback_rate(self):
        """Cashback rate (if applicable)."""
        if random.random() < 0.5:
            return round(random.uniform(1.0, 5.0), 1)
        return None
    
    def credit_card_cardholder_name(self):
        """Cardholder name."""
        return self.fake.name()
    
    def credit_card_expires(self):
        """Card expiration date."""
        future_date = datetime.now() + timedelta(days=random.randint(365, 1825))
        return future_date.strftime("%Y-%m")
    
    def credit_card_date_issued(self):
        """Date card was issued."""
        return self.common_date(start_year=2015, end_year=2024)


def create_credit_card_data(num_entities=10, seed=None):
    """
    Generate credit card data using the custom provider.
    
    Args:
        num_entities: Number of credit card entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing credit card data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgCreditCardProvider)
    
    cards = []
    
    for i in range(num_entities):
        card = {
            "@type": "CreditCard",
            "name": fake.credit_card_name(),
            "description": fake.credit_card_description(),
        }
        
        # Optional properties
        if random.random() < 0.8:
            card["cardNumber"] = fake.credit_card_card_number()
        
        if random.random() < 0.9:
            card["issuer"] = fake.credit_card_issuer()
        
        if random.random() < 0.8:
            card["annualPercentageRate"] = fake.credit_card_annual_percentage_rate()
        
        if random.random() < 0.7:
            card["creditLimit"] = fake.credit_card_credit_limit()
        
        if random.random() < 0.8:
            card["currency"] = fake.credit_card_currency()
        
        if random.random() < 0.7:
            card["interestRate"] = fake.credit_card_interest_rate()
        
        if random.random() < 0.6:
            card["annualFee"] = fake.credit_card_annual_fee()
        
        if random.random() < 0.4:
            cashback = fake.credit_card_cashback_rate()
            if cashback:
                card["cashbackRate"] = cashback
        
        if random.random() < 0.8:
            card["cardholderName"] = fake.credit_card_cardholder_name()
        
        if random.random() < 0.7:
            card["expires"] = fake.credit_card_expires()
        
        if random.random() < 0.6:
            card["dateIssued"] = fake.credit_card_date_issued()
        
        cards.append(card)
    
    return cards


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org CreditCard Provider\n")
    print("=" * 80)
    
    cards = create_credit_card_data(num_entities=3, seed=42)
    
    for i, card in enumerate(cards, 1):
        print(f"\nCreditCard {i}:")
        print("-" * 80)
        for key, value in card.items():
            print(f"  {key}: {value}")

