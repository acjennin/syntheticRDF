"""
Custom Faker provider for Schema.org/BrokerageAccount properties.
Generates realistic data for brokerage accounts (specialization of FinancialProduct).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgBrokerageAccountProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/BrokerageAccount properties."""
    
    # BrokerageAccount-specific data
    BROKERAGE_FIRMS = [
        "Fidelity Investments", "Charles Schwab", "Vanguard",
        "TD Ameritrade", "E*TRADE", "Merrill Lynch", "Interactive Brokers",
        "Robinhood", "Ally Invest", "Webull"
    ]
    
    ACCOUNT_TYPES = [
        "Individual", "Joint", "IRA", "Roth IRA", "401(k)", "Trust",
        "Corporate", "Custodial"
    ]
    
    def brokerage_account_name(self):
        """Brokerage account name."""
        return f"{random.choice(self.ACCOUNT_TYPES)} Brokerage Account"
    
    def brokerage_account_account_number(self):
        """Account number."""
        return f"{random.randint(100000000, 999999999999)}"
    
    def brokerage_account_broker(self):
        """Brokerage firm."""
        return random.choice(self.BROKERAGE_FIRMS)
    
    def brokerage_account_currency(self):
        """Account currency."""
        return self.common_currency_code()
    
    def brokerage_account_balance(self):
        """Account balance."""
        balance_ranges = [
            (0, 10000, 0.2),
            (10000, 50000, 0.3),
            (50000, 250000, 0.25),
            (250000, 1000000, 0.15),
            (1000000, 5000000, 0.08),
            (5000000, 10000000, 0.02)
        ]
        
        rand = random.random()
        cumulative = 0
        for min_bal, max_bal, prob in balance_ranges:
            cumulative += prob
            if rand <= cumulative:
                return round(random.uniform(min_bal, max_bal), 2)
        
        return round(random.uniform(0, 50000), 2)
    
    def brokerage_account_annual_percentage_rate(self):
        """Annual Percentage Rate."""
        return round(random.uniform(0.0, 5.0), 2)
    
    def brokerage_account_fees_and_commissions_specification(self):
        """Fees and commissions."""
        return {
            "commissionPerTrade": round(random.uniform(0, 10), 2),
            "annualFee": round(random.uniform(0, 100), 2),
            "inactivityFee": round(random.uniform(0, 50), 2)
        }
    
    def brokerage_account_opening_date(self):
        """Account opening date."""
        return self.common_date(start_year=2000, end_year=2024)
    
    def brokerage_account_account_holder(self):
        """Account holder name."""
        return self.fake.name()


def create_brokerage_account_data(num_entities=10, seed=None):
    """
    Generate brokerage account data using the custom provider.
    
    Args:
        num_entities: Number of brokerage account entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing brokerage account data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgBrokerageAccountProvider)
    
    accounts = []
    
    for i in range(num_entities):
        account = {
            "@type": "BrokerageAccount",
            "name": fake.brokerage_account_name(),
            "accountNumber": fake.brokerage_account_account_number(),
            "broker": fake.brokerage_account_broker(),
        }
        
        # Optional properties
        account["currency"] = fake.brokerage_account_currency()
        
        if random.random() < 0.8:
            account["balance"] = fake.brokerage_account_balance()
        
        if random.random() < 0.6:
            account["annualPercentageRate"] = fake.brokerage_account_annual_percentage_rate()
        
        if random.random() < 0.5:
            account["feesAndCommissionsSpecification"] = fake.brokerage_account_fees_and_commissions_specification()
        
        account["openingDate"] = fake.brokerage_account_opening_date()
        account["accountHolder"] = fake.brokerage_account_account_holder()
        
        accounts.append(account)
    
    return accounts


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org BrokerageAccount Provider\n")
    print("=" * 80)
    
    accounts = create_brokerage_account_data(num_entities=3, seed=42)
    
    for i, account in enumerate(accounts, 1):
        print(f"\nBrokerageAccount {i}:")
        print("-" * 80)
        for key, value in account.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

