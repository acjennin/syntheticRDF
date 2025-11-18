"""
Custom Faker provider for Schema.org/InvestmentOrDeposit properties.
Generates realistic data for investment and deposit products.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgInvestmentOrDepositProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/InvestmentOrDeposit properties."""
    
    # InvestmentOrDeposit-specific data
    INVESTMENT_TYPES = [
        "Savings Account", "Certificate of Deposit", "Money Market Account",
        "Mutual Fund", "Stocks", "Bonds", "ETF", "IRA", "401(k)"
    ]
    
    RISK_LEVELS = [
        "Low", "Medium", "High", "Very High"
    ]
    
    def investment_or_deposit_name(self):
        """Investment or deposit name."""
        types = ["Premium", "Growth", "Conservative", "Aggressive", "Balanced"]
        return f"{random.choice(types)} {random.choice(self.INVESTMENT_TYPES)}"
    
    def investment_or_deposit_description(self):
        """Investment or deposit description."""
        return self.common_description()
    
    def investment_or_deposit_amount(self):
        """Investment amount."""
        amounts = [
            (1000, 10000, 0.3),
            (10000, 50000, 0.3),
            (50000, 100000, 0.2),
            (100000, 500000, 0.15),
            (500000, 1000000, 0.05)
        ]
        
        rand = random.random()
        cumulative = 0
        for min_amt, max_amt, prob in amounts:
            cumulative += prob
            if rand <= cumulative:
                return round(random.uniform(min_amt, max_amt), 2)
        
        return round(random.uniform(1000, 10000), 2)
    
    def investment_or_deposit_interest_rate(self):
        """Interest rate or expected return."""
        return round(random.uniform(0.5, 15.0), 2)
    
    def investment_or_deposit_annual_percentage_rate(self):
        """Annual Percentage Rate."""
        return round(random.uniform(1.0, 20.0), 2)
    
    def investment_or_deposit_risk_level(self):
        """Risk level."""
        return random.choice(self.RISK_LEVELS)
    
    def investment_or_deposit_provider(self):
        """Investment provider."""
        providers = [
            "Fidelity Investments", "Charles Schwab", "Vanguard",
            "TD Ameritrade", "E*TRADE", "Merrill Lynch"
        ]
        return random.choice(providers)
    
    def investment_or_deposit_currency(self):
        """Currency."""
        return self.common_currency_code()
    
    def investment_or_deposit_term(self):
        """Investment term."""
        terms = ["1 Year", "3 Years", "5 Years", "10 Years", "No Term"]
        return random.choice(terms)
    
    def investment_or_deposit_minimum_investment(self):
        """Minimum investment amount."""
        minimums = [100, 500, 1000, 2500, 5000, 10000]
        return random.choice(minimums)


def create_investment_or_deposit_data(num_entities=10, seed=None):
    """
    Generate investment or deposit data using the custom provider.
    
    Args:
        num_entities: Number of investment/deposit entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing investment or deposit data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgInvestmentOrDepositProvider)
    
    investments = []
    
    for i in range(num_entities):
        investment = {
            "@type": "InvestmentOrDeposit",
            "name": fake.investment_or_deposit_name(),
            "description": fake.investment_or_deposit_description(),
        }
        
        # Optional properties
        if random.random() < 0.8:
            investment["amount"] = fake.investment_or_deposit_amount()
        
        if random.random() < 0.7:
            investment["interestRate"] = fake.investment_or_deposit_interest_rate()
        
        if random.random() < 0.6:
            investment["annualPercentageRate"] = fake.investment_or_deposit_annual_percentage_rate()
        
        if random.random() < 0.7:
            investment["riskLevel"] = fake.investment_or_deposit_risk_level()
        
        if random.random() < 0.8:
            investment["provider"] = fake.investment_or_deposit_provider()
        
        if random.random() < 0.7:
            investment["currency"] = fake.investment_or_deposit_currency()
        
        if random.random() < 0.5:
            investment["term"] = fake.investment_or_deposit_term()
        
        if random.random() < 0.6:
            investment["minimumInvestment"] = fake.investment_or_deposit_minimum_investment()
        
        investments.append(investment)
    
    return investments


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org InvestmentOrDeposit Provider\n")
    print("=" * 80)
    
    investments = create_investment_or_deposit_data(num_entities=3, seed=42)
    
    for i, investment in enumerate(investments, 1):
        print(f"\nInvestmentOrDeposit {i}:")
        print("-" * 80)
        for key, value in investment.items():
            print(f"  {key}: {value}")

