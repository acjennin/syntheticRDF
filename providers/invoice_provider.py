"""
Custom Faker provider for Schema.org/Invoice properties.
Generates realistic data for invoices and billing documents.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgInvoiceProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Invoice properties."""
    
    # Invoice-specific data
    PAYMENT_STATUSES = [
        "PaymentAutomaticallyApplied",
        "PaymentComplete",
        "PaymentDeclined",
        "PaymentDue",
        "PaymentPastDue"
    ]
    
    PAYMENT_METHODS = [
        "Credit Card", "Debit Card", "Bank Transfer", "Check",
        "Cash", "PayPal", "Wire Transfer", "ACH"
    ]
    
    def invoice_invoice_number(self):
        """Invoice number."""
        prefix = random.choice(["INV", "IN", "BILL"])
        number = random.randint(100000, 999999)
        return f"{prefix}-{number}"
    
    def invoice_billing_period(self):
        """Billing period."""
        start_date = datetime.now() - timedelta(days=random.randint(30, 90))
        end_date = start_date + timedelta(days=30)
        return {
            "startDate": start_date.isoformat(),
            "endDate": end_date.isoformat()
        }
    
    def invoice_total_payment_due(self):
        """Total payment due."""
        return self.common_price(min_value=50, max_value=10000)
    
    def invoice_payment_due_date(self):
        """Payment due date."""
        future_date = datetime.now() + timedelta(days=random.randint(1, 30))
        return future_date.isoformat()
    
    def invoice_account_id(self):
        """Account ID."""
        return f"ACC-{random.randint(100000, 999999)}"
    
    def invoice_payment_status(self):
        """Payment status."""
        return random.choice(self.PAYMENT_STATUSES)
    
    def invoice_provider(self):
        """Invoice provider (organization issuing the invoice)."""
        return self.fake.company()
    
    def invoice_customer(self):
        """Customer (person or organization)."""
        return self.fake.name()
    
    def invoice_references_order(self):
        """Order number this invoice references."""
        prefix = random.choice(["ORD", "PO", "ORDER"])
        number = random.randint(100000, 999999)
        return f"{prefix}-{number}"
    
    def invoice_payment_method(self):
        """Payment method."""
        return random.choice(self.PAYMENT_METHODS)
    
    def invoice_date_issued(self):
        """Date invoice was issued."""
        past_date = datetime.now() - timedelta(days=random.randint(0, 30))
        return past_date.isoformat()
    
    def invoice_minimum_payment_due(self, total_due=None):
        """Minimum payment due."""
        if total_due:
            return round(total_due * random.uniform(0.1, 0.5), 2)
        return self.common_price(min_value=10, max_value=500)
    
    def invoice_category(self):
        """Invoice category."""
        categories = [
            "Service", "Product", "Subscription", "Rental", "Utility",
            "Professional Services", "Consulting", "Maintenance"
        ]
        return random.choice(categories)


def create_invoice_data(num_entities=10, seed=None):
    """
    Generate invoice data using the custom provider.
    
    Args:
        num_entities: Number of invoice entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing invoice data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgInvoiceProvider)
    
    invoices = []
    
    for i in range(num_entities):
        total_due = fake.invoice_total_payment_due()
        payment_due_date = fake.invoice_payment_due_date()
        
        invoice = {
            "@type": "Invoice",
            "invoiceNumber": fake.invoice_invoice_number(),
            "totalPaymentDue": total_due,
            "paymentDueDate": payment_due_date,
        }
        
        # Optional properties
        if random.random() < 0.7:
            invoice["billingPeriod"] = fake.invoice_billing_period()
        
        if random.random() < 0.8:
            invoice["accountId"] = fake.invoice_account_id()
        
        invoice["paymentStatus"] = fake.invoice_payment_status()
        
        if random.random() < 0.9:
            invoice["provider"] = fake.invoice_provider()
        
        if random.random() < 0.9:
            invoice["customer"] = fake.invoice_customer()
        
        if random.random() < 0.6:
            invoice["referencesOrder"] = fake.invoice_references_order()
        
        if random.random() < 0.7:
            invoice["paymentMethod"] = fake.invoice_payment_method()
        
        if random.random() < 0.8:
            invoice["dateIssued"] = fake.invoice_date_issued()
        
        if random.random() < 0.5:
            invoice["minimumPaymentDue"] = fake.invoice_minimum_payment_due(total_due)
        
        if random.random() < 0.6:
            invoice["category"] = fake.invoice_category()
        
        # Currency
        invoice["priceCurrency"] = fake.common_currency_code()
        
        invoices.append(invoice)
    
    return invoices


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Invoice Provider\n")
    print("=" * 80)
    
    invoices = create_invoice_data(num_entities=3, seed=42)
    
    for i, invoice in enumerate(invoices, 1):
        print(f"\nInvoice {i}:")
        print("-" * 80)
        for key, value in invoice.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

