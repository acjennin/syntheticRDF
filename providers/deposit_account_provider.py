"""
Custom Faker provider for Schema.org/DepositAccount properties.
Generates realistic data for deposit accounts (specialization of BankAccount).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgDepositAccountProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/DepositAccount properties."""
    
    # DepositAccount-specific data
    DEPOSIT_ACCOUNT_TYPES = [
        "Savings Account",
        "Checking Account",
        "Money Market Account",
        "Certificate of Deposit",
        "Time Deposit",
        "Demand Deposit"
    ]
    
    BANKS = [
        "Chase Bank", "Bank of America", "Wells Fargo", "Citibank",
        "US Bank", "PNC Bank", "Capital One", "TD Bank"
    ]
    
    def deposit_account_name(self):
        """Deposit account name."""
        types = ["Premium", "Standard", "High Yield", "Basic"]
        return f"{random.choice(types)} {random.choice(self.DEPOSIT_ACCOUNT_TYPES)}"
    
    def deposit_account_account_number(self):
        """Account number."""
        return f"{random.randint(10000000, 999999999999)}"
    
    def deposit_account_bank_name(self):
        """Bank name."""
        return random.choice(self.BANKS)
    
    def deposit_account_currency(self):
        """Account currency."""
        return self.common_currency_code()
    
    def deposit_account_balance(self):
        """Current balance."""
        balance_ranges = [
            (0, 1000, 0.2),
            (1000, 10000, 0.3),
            (10000, 50000, 0.25),
            (50000, 100000, 0.15),
            (100000, 500000, 0.07),
            (500000, 1000000, 0.03)
        ]
        
        rand = random.random()
        cumulative = 0
        for min_bal, max_bal, prob in balance_ranges:
            cumulative += prob
            if rand <= cumulative:
                return round(random.uniform(min_bal, max_bal), 2)
        
        return round(random.uniform(0, 10000), 2)
    
    def deposit_account_interest_rate(self):
        """Interest rate."""
        return round(random.uniform(0.01, 5.0), 2)
    
    def deposit_account_minimum_balance(self):
        """Minimum balance requirement."""
        minimums = [0, 25, 100, 500, 1000, 2500]
        return random.choice(minimums)
    
    def deposit_account_opening_date(self):
        """Account opening date."""
        return self.common_date(start_year=1990, end_year=2024)
    
    def deposit_account_account_holder(self):
        """Account holder name."""
        return self.fake.name()


def create_deposit_account_data(num_entities=10, seed=None):
    """
    Generate deposit account data using the custom provider.
    
    Args:
        num_entities: Number of deposit account entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing deposit account data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgDepositAccountProvider)
    
    accounts = []
    
    for i in range(num_entities):
        account = {
            "@type": "DepositAccount",
            "name": fake.deposit_account_name(),
            "accountNumber": fake.deposit_account_account_number(),
            "bankName": fake.deposit_account_bank_name(),
        }
        
        # Optional properties
        account["currency"] = fake.deposit_account_currency()
        
        if random.random() < 0.8:
            account["balance"] = fake.deposit_account_balance()
        
        if random.random() < 0.6:
            account["interestRate"] = fake.deposit_account_interest_rate()
        
        if random.random() < 0.5:
            account["minimumBalance"] = fake.deposit_account_minimum_balance()
        
        account["openingDate"] = fake.deposit_account_opening_date()
        account["accountHolder"] = fake.deposit_account_account_holder()
        
        accounts.append(account)
    
    return accounts


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org DepositAccount Provider\n")
    print("=" * 80)
    
    accounts = create_deposit_account_data(num_entities=3, seed=42)
    
    for i, account in enumerate(accounts, 1):
        print(f"\nDepositAccount {i}:")
        print("-" * 80)
        for key, value in account.items():
            print(f"  {key}: {value}")

