"""
Custom Faker provider for Schema.org/LoanOrCredit properties.
Generates realistic data for loans and credit products (base class).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgLoanOrCreditProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/LoanOrCredit properties."""
    
    # LoanOrCredit-specific data
    LOAN_TYPES = [
        "Personal Loan", "Auto Loan", "Student Loan", "Home Loan",
        "Business Loan", "Credit Line", "Revolving Credit"
    ]
    
    def loan_or_credit_name(self):
        """Loan or credit name."""
        return random.choice(self.LOAN_TYPES)
    
    def loan_or_credit_description(self):
        """Loan or credit description."""
        return self.common_description()
    
    def loan_or_credit_amount(self):
        """Loan amount."""
        amounts = [
            (1000, 10000, 0.3),
            (10000, 50000, 0.3),
            (50000, 100000, 0.2),
            (100000, 500000, 0.15),
            (500000, 2000000, 0.05)
        ]
        
        rand = random.random()
        cumulative = 0
        for min_amt, max_amt, prob in amounts:
            cumulative += prob
            if rand <= cumulative:
                return round(random.uniform(min_amt, max_amt), 2)
        
        return round(random.uniform(1000, 10000), 2)
    
    def loan_or_credit_annual_percentage_rate(self):
        """Annual Percentage Rate (APR)."""
        return round(random.uniform(3.0, 30.0), 2)
    
    def loan_or_credit_interest_rate(self):
        """Interest rate."""
        return round(random.uniform(2.0, 25.0), 2)
    
    def loan_or_credit_currency(self):
        """Currency."""
        return self.common_currency_code()
    
    def loan_or_credit_loan_term(self):
        """Loan term."""
        terms = ["12 months", "24 months", "36 months", "48 months", "60 months", "120 months", "240 months", "360 months"]
        return random.choice(terms)
    
    def loan_or_credit_loan_type(self):
        """Type of loan."""
        return random.choice(self.LOAN_TYPES)
    
    def loan_or_credit_lender(self):
        """Lender name."""
        lenders = [
            "Chase Bank", "Bank of America", "Wells Fargo", "Citibank",
            "Capital One", "Discover", "American Express", "US Bank"
        ]
        return random.choice(lenders)
    
    def loan_or_credit_borrower(self):
        """Borrower name."""
        return self.fake.name()
    
    def loan_or_credit_date_issued(self):
        """Date loan was issued."""
        return self.common_date(start_year=2010, end_year=2024)
    
    def loan_or_credit_grace_period(self):
        """Grace period."""
        periods = ["0 days", "30 days", "60 days", "90 days"]
        return random.choice(periods)
    
    def loan_or_credit_required_collateral(self):
        """Required collateral."""
        collaterals = ["None", "Vehicle", "Property", "Savings Account", "Certificate of Deposit"]
        return random.choice(collaterals)


def create_loan_or_credit_data(num_entities=10, seed=None):
    """
    Generate loan or credit data using the custom provider.
    
    Args:
        num_entities: Number of loan/credit entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing loan or credit data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgLoanOrCreditProvider)
    
    loans = []
    
    for i in range(num_entities):
        loan = {
            "@type": "LoanOrCredit",
            "name": fake.loan_or_credit_name(),
            "description": fake.loan_or_credit_description(),
        }
        
        # Optional properties
        if random.random() < 0.9:
            loan["amount"] = fake.loan_or_credit_amount()
        
        if random.random() < 0.8:
            loan["annualPercentageRate"] = fake.loan_or_credit_annual_percentage_rate()
        
        if random.random() < 0.7:
            loan["interestRate"] = fake.loan_or_credit_interest_rate()
        
        if random.random() < 0.8:
            loan["currency"] = fake.loan_or_credit_currency()
        
        if random.random() < 0.7:
            loan["loanTerm"] = fake.loan_or_credit_loan_term()
        
        if random.random() < 0.8:
            loan["loanType"] = fake.loan_or_credit_loan_type()
        
        if random.random() < 0.9:
            loan["lender"] = fake.loan_or_credit_lender()
        
        if random.random() < 0.8:
            loan["borrower"] = fake.loan_or_credit_borrower()
        
        if random.random() < 0.7:
            loan["dateIssued"] = fake.loan_or_credit_date_issued()
        
        if random.random() < 0.5:
            loan["gracePeriod"] = fake.loan_or_credit_grace_period()
        
        if random.random() < 0.4:
            loan["requiredCollateral"] = fake.loan_or_credit_required_collateral()
        
        loans.append(loan)
    
    return loans


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org LoanOrCredit Provider\n")
    print("=" * 80)
    
    loans = create_loan_or_credit_data(num_entities=3, seed=42)
    
    for i, loan in enumerate(loans, 1):
        print(f"\nLoanOrCredit {i}:")
        print("-" * 80)
        for key, value in loan.items():
            print(f"  {key}: {value}")

