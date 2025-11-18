"""
Custom Faker provider for Schema.org/FinancialProduct properties.
Generates realistic data for financial products (base class for various financial instruments).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgFinancialProductProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/FinancialProduct properties."""
    
    # FinancialProduct-specific data
    FINANCIAL_PRODUCT_TYPES = [
        "BankAccount", "DepositAccount", "BrokerageAccount",
        "InvestmentFund", "LoanOrCredit", "CreditCard",
        "MortgageLoan", "PaymentCard"
    ]
    
    INTEREST_RATES = [
        "Fixed", "Variable", "Prime", "LIBOR", "Treasury"
    ]
    
    def financial_product_name(self):
        """Financial product name."""
        types = ["Premium", "Standard", "Basic", "Elite", "Professional"]
        products = ["Account", "Product", "Service", "Plan"]
        return f"{random.choice(types)} {random.choice(products)}"
    
    def financial_product_description(self):
        """Financial product description."""
        return self.common_description()
    
    def financial_product_annual_percentage_rate(self):
        """Annual Percentage Rate (APR)."""
        return round(random.uniform(0.5, 25.0), 2)
    
    def financial_product_fees_and_commissions_specification(self):
        """Fees and commissions."""
        fees = {
            "monthlyFee": round(random.uniform(0, 25), 2),
            "annualFee": round(random.uniform(0, 200), 2),
            "transactionFee": round(random.uniform(0, 5), 2),
            "overdraftFee": round(random.uniform(25, 50), 2)
        }
        return fees
    
    def financial_product_interest_rate(self):
        """Interest rate."""
        return round(random.uniform(0.01, 10.0), 2)
    
    def financial_product_interest_rate_type(self):
        """Type of interest rate."""
        return random.choice(self.INTEREST_RATES)
    
    def financial_product_provider(self):
        """Financial product provider."""
        return self.fake.company()
    
    def financial_product_currency(self):
        """Currency."""
        return self.common_currency_code()
    
    def financial_product_terms_of_service(self):
        """Terms of service URL."""
        return self.common_url()


def create_financial_product_data(num_entities=10, seed=None):
    """
    Generate financial product data using the custom provider.
    
    Args:
        num_entities: Number of financial product entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing financial product data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgFinancialProductProvider)
    
    products = []
    
    for i in range(num_entities):
        product = {
            "@type": "FinancialProduct",
            "name": fake.financial_product_name(),
            "description": fake.financial_product_description(),
        }
        
        # Optional properties
        if random.random() < 0.7:
            product["annualPercentageRate"] = fake.financial_product_annual_percentage_rate()
        
        if random.random() < 0.6:
            product["feesAndCommissionsSpecification"] = fake.financial_product_fees_and_commissions_specification()
        
        if random.random() < 0.7:
            product["interestRate"] = fake.financial_product_interest_rate()
        
        if random.random() < 0.5:
            product["interestRateType"] = fake.financial_product_interest_rate_type()
        
        if random.random() < 0.8:
            product["provider"] = fake.financial_product_provider()
        
        if random.random() < 0.7:
            product["currency"] = fake.financial_product_currency()
        
        if random.random() < 0.5:
            product["termsOfService"] = fake.financial_product_terms_of_service()
        
        products.append(product)
    
    return products


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org FinancialProduct Provider\n")
    print("=" * 80)
    
    products = create_financial_product_data(num_entities=3, seed=42)
    
    for i, product in enumerate(products, 1):
        print(f"\nFinancialProduct {i}:")
        print("-" * 80)
        for key, value in product.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

