"""
Custom Faker provider for Schema.org/MortgageLoan properties.
Generates realistic data for mortgage loans (specialization of LoanOrCredit).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgMortgageLoanProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/MortgageLoan properties."""
    
    # MortgageLoan-specific data
    MORTGAGE_TYPES = [
        "Fixed Rate Mortgage", "Adjustable Rate Mortgage (ARM)",
        "FHA Loan", "VA Loan", "Conventional Loan", "Jumbo Loan"
    ]
    
    LENDERS = [
        "Quicken Loans", "Wells Fargo", "Bank of America", "Chase",
        "US Bank", "PNC Bank", "Citibank", "Rocket Mortgage"
    ]
    
    def mortgage_loan_name(self):
        """Mortgage loan name."""
        return random.choice(self.MORTGAGE_TYPES)
    
    def mortgage_loan_description(self):
        """Mortgage loan description."""
        return self.common_description()
    
    def mortgage_loan_amount(self):
        """Loan amount."""
        amounts = [
            (50000, 200000, 0.2),
            (200000, 400000, 0.3),
            (400000, 600000, 0.25),
            (600000, 1000000, 0.15),
            (1000000, 2000000, 0.08),
            (2000000, 5000000, 0.02)
        ]
        
        rand = random.random()
        cumulative = 0
        for min_amt, max_amt, prob in amounts:
            cumulative += prob
            if rand <= cumulative:
                return round(random.uniform(min_amt, max_amt), 2)
        
        return round(random.uniform(200000, 400000), 2)
    
    def mortgage_loan_annual_percentage_rate(self):
        """Annual Percentage Rate (APR)."""
        return round(random.uniform(2.5, 6.5), 2)
    
    def mortgage_loan_interest_rate(self):
        """Interest rate."""
        return round(random.uniform(2.0, 6.0), 2)
    
    def mortgage_loan_loan_term(self):
        """Loan term."""
        terms = ["15 years", "20 years", "30 years"]
        return random.choice(terms)
    
    def mortgage_loan_currency(self):
        """Currency."""
        return self.common_currency_code()
    
    def mortgage_loan_lender(self):
        """Lender name."""
        return random.choice(self.LENDERS)
    
    def mortgage_loan_borrower(self):
        """Borrower name."""
        return self.fake.name()
    
    def mortgage_loan_down_payment(self, loan_amount=None):
        """Down payment amount."""
        if loan_amount:
            # Typically 5-20% down payment
            down_payment_pct = random.uniform(0.05, 0.20)
            return round(loan_amount * down_payment_pct, 2)
        return round(random.uniform(10000, 100000), 2)
    
    def mortgage_loan_monthly_payment(self, loan_amount=None, interest_rate=None, term_years=None):
        """Monthly payment (simplified calculation)."""
        if loan_amount and interest_rate and term_years:
            # Simplified mortgage payment calculation
            monthly_rate = interest_rate / 100 / 12
            num_payments = term_years * 12
            if monthly_rate > 0:
                monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
                return round(monthly_payment, 2)
        return round(random.uniform(1000, 5000), 2)
    
    def mortgage_loan_property_address(self):
        """Property address."""
        return self.common_address()
    
    def mortgage_loan_date_issued(self):
        """Date loan was issued."""
        return self.common_date(start_year=2010, end_year=2024)
    
    def mortgage_loan_loan_type(self):
        """Type of mortgage."""
        return random.choice(self.MORTGAGE_TYPES)


def create_mortgage_loan_data(num_entities=10, seed=None):
    """
    Generate mortgage loan data using the custom provider.
    
    Args:
        num_entities: Number of mortgage loan entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing mortgage loan data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgMortgageLoanProvider)
    
    mortgages = []
    
    for i in range(num_entities):
        loan_amount = fake.mortgage_loan_amount()
        interest_rate = fake.mortgage_loan_interest_rate()
        term_str = fake.mortgage_loan_loan_term()
        term_years = int(term_str.split()[0])
        
        mortgage = {
            "@type": "MortgageLoan",
            "name": fake.mortgage_loan_name(),
            "description": fake.mortgage_loan_description(),
            "amount": loan_amount,
        }
        
        # Optional properties
        if random.random() < 0.9:
            mortgage["annualPercentageRate"] = fake.mortgage_loan_annual_percentage_rate()
        
        if random.random() < 0.8:
            mortgage["interestRate"] = interest_rate
        
        if random.random() < 0.9:
            mortgage["loanTerm"] = term_str
        
        if random.random() < 0.8:
            mortgage["currency"] = fake.mortgage_loan_currency()
        
        if random.random() < 0.9:
            mortgage["lender"] = fake.mortgage_loan_lender()
        
        if random.random() < 0.8:
            mortgage["borrower"] = fake.mortgage_loan_borrower()
        
        if random.random() < 0.7:
            mortgage["downPayment"] = fake.mortgage_loan_down_payment(loan_amount)
        
        if random.random() < 0.7:
            mortgage["monthlyPayment"] = fake.mortgage_loan_monthly_payment(loan_amount, interest_rate, term_years)
        
        if random.random() < 0.8:
            mortgage["propertyAddress"] = fake.mortgage_loan_property_address()
        
        if random.random() < 0.7:
            mortgage["dateIssued"] = fake.mortgage_loan_date_issued()
        
        if random.random() < 0.8:
            mortgage["loanType"] = fake.mortgage_loan_loan_type()
        
        mortgages.append(mortgage)
    
    return mortgages


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org MortgageLoan Provider\n")
    print("=" * 80)
    
    mortgages = create_mortgage_loan_data(num_entities=3, seed=42)
    
    for i, mortgage in enumerate(mortgages, 1):
        print(f"\nMortgageLoan {i}:")
        print("-" * 80)
        for key, value in mortgage.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

