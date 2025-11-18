"""
Custom Faker provider for Schema.org/InvestmentFund properties.
Generates realistic data for investment funds (mutual funds, ETFs, etc.).
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgInvestmentFundProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/InvestmentFund properties."""
    
    # InvestmentFund-specific data
    FUND_TYPES = [
        "Mutual Fund", "Exchange-Traded Fund (ETF)", "Index Fund",
        "Hedge Fund", "Money Market Fund", "Bond Fund", "Stock Fund",
        "Balanced Fund", "Target Date Fund"
    ]
    
    FUND_CATEGORIES = [
        "Growth", "Value", "Income", "Blend", "Large Cap", "Mid Cap",
        "Small Cap", "International", "Emerging Markets", "Sector"
    ]
    
    FUND_COMPANIES = [
        "Vanguard", "Fidelity", "BlackRock", "State Street",
        "T. Rowe Price", "American Funds", "JPMorgan", "Goldman Sachs"
    ]
    
    def investment_fund_name(self):
        """Investment fund name."""
        categories = ["Growth", "Value", "Income", "Balanced", "Index"]
        types = ["Fund", "ETF", "Portfolio"]
        return f"{random.choice(categories)} {random.choice(types)}"
    
    def investment_fund_description(self):
        """Investment fund description."""
        return self.common_description()
    
    def investment_fund_fund_type(self):
        """Type of fund."""
        return random.choice(self.FUND_TYPES)
    
    def investment_fund_category(self):
        """Fund category."""
        return random.choice(self.FUND_CATEGORIES)
    
    def investment_fund_provider(self):
        """Fund provider/company."""
        return random.choice(self.FUND_COMPANIES)
    
    def investment_fund_net_asset_value(self):
        """Net Asset Value (NAV) per share."""
        return round(random.uniform(10.0, 500.0), 2)
    
    def investment_fund_expense_ratio(self):
        """Expense ratio (annual fee as percentage)."""
        return round(random.uniform(0.05, 2.5), 2)
    
    def investment_fund_annual_percentage_rate(self):
        """Annual Percentage Rate."""
        return round(random.uniform(3.0, 15.0), 2)
    
    def investment_fund_minimum_investment(self):
        """Minimum investment amount."""
        minimums = [100, 500, 1000, 2500, 5000, 10000]
        return random.choice(minimums)
    
    def investment_fund_currency(self):
        """Currency."""
        return self.common_currency_code()
    
    def investment_fund_risk_level(self):
        """Risk level."""
        levels = ["Low", "Medium", "High", "Very High"]
        return random.choice(levels)
    
    def investment_fund_date_established(self):
        """Date fund was established."""
        return self.common_date(start_year=1950, end_year=2020)


def create_investment_fund_data(num_entities=10, seed=None):
    """
    Generate investment fund data using the custom provider.
    
    Args:
        num_entities: Number of investment fund entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing investment fund data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgInvestmentFundProvider)
    
    funds = []
    
    for i in range(num_entities):
        fund = {
            "@type": "InvestmentFund",
            "name": fake.investment_fund_name(),
            "description": fake.investment_fund_description(),
            "fundType": fake.investment_fund_fund_type(),
        }
        
        # Optional properties
        if random.random() < 0.8:
            fund["category"] = fake.investment_fund_category()
        
        if random.random() < 0.9:
            fund["provider"] = fake.investment_fund_provider()
        
        if random.random() < 0.7:
            fund["netAssetValue"] = fake.investment_fund_net_asset_value()
        
        if random.random() < 0.8:
            fund["expenseRatio"] = fake.investment_fund_expense_ratio()
        
        if random.random() < 0.6:
            fund["annualPercentageRate"] = fake.investment_fund_annual_percentage_rate()
        
        if random.random() < 0.7:
            fund["minimumInvestment"] = fake.investment_fund_minimum_investment()
        
        if random.random() < 0.7:
            fund["currency"] = fake.investment_fund_currency()
        
        if random.random() < 0.7:
            fund["riskLevel"] = fake.investment_fund_risk_level()
        
        if random.random() < 0.6:
            fund["dateEstablished"] = fake.investment_fund_date_established()
        
        funds.append(fund)
    
    return funds


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org InvestmentFund Provider\n")
    print("=" * 80)
    
    funds = create_investment_fund_data(num_entities=3, seed=42)
    
    for i, fund in enumerate(funds, 1):
        print(f"\nInvestmentFund {i}:")
        print("-" * 80)
        for key, value in fund.items():
            print(f"  {key}: {value}")

