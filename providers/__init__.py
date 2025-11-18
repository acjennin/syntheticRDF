"""
Custom Faker providers for Schema.org ontologies.

This package provides Faker-based data generators for various Schema.org types.
All providers inherit from BaseSchemaOrgProvider which provides common properties
that can be reused across different Schema.org types.
"""

from .base_provider import BaseSchemaOrgProvider, create_faker_with_base
from .person_provider import SchemaOrgPersonProvider, create_person_data
from .organization_provider import SchemaOrgOrganizationProvider, create_organization_data
from .bank_account_provider import SchemaOrgBankAccountProvider, create_bank_account_data
from .order_provider import SchemaOrgOrderProvider, create_order_data
from .product_provider import SchemaOrgProductProvider, create_product_data
from .place_provider import SchemaOrgPlaceProvider, create_place_data
from .event_provider import SchemaOrgEventProvider, create_event_data
from .offer_provider import SchemaOrgOfferProvider, create_offer_data
from .review_provider import SchemaOrgReviewProvider, create_review_data, create_aggregate_rating_data
from .local_business_provider import SchemaOrgLocalBusinessProvider, create_local_business_data
from .course_provider import SchemaOrgCourseProvider, create_course_data
from .job_posting_provider import SchemaOrgJobPostingProvider, create_job_posting_data
from .article_provider import SchemaOrgArticleProvider, create_article_data
from .book_provider import SchemaOrgBookProvider, create_book_data
from .invoice_provider import SchemaOrgInvoiceProvider, create_invoice_data
from .restaurant_provider import SchemaOrgRestaurantProvider, create_restaurant_data
from .hotel_provider import SchemaOrgHotelProvider, create_hotel_data
from .software_application_provider import SchemaOrgSoftwareApplicationProvider, create_software_application_data
from .recipe_provider import SchemaOrgRecipeProvider, create_recipe_data
from .financial_product_provider import SchemaOrgFinancialProductProvider, create_financial_product_data
from .deposit_account_provider import SchemaOrgDepositAccountProvider, create_deposit_account_data
from .currency_conversion_service_provider import SchemaOrgCurrencyConversionServiceProvider, create_currency_conversion_service_data
from .investment_or_deposit_provider import SchemaOrgInvestmentOrDepositProvider, create_investment_or_deposit_data
from .brokerage_account_provider import SchemaOrgBrokerageAccountProvider, create_brokerage_account_data
from .investment_fund_provider import SchemaOrgInvestmentFundProvider, create_investment_fund_data
from .loan_or_credit_provider import SchemaOrgLoanOrCreditProvider, create_loan_or_credit_data
from .credit_card_provider import SchemaOrgCreditCardProvider, create_credit_card_data
from .mortgage_loan_provider import SchemaOrgMortgageLoanProvider, create_mortgage_loan_data
from .payment_card_provider import SchemaOrgPaymentCardProvider, create_payment_card_data
from .payment_service_provider import SchemaOrgPaymentServiceProvider, create_payment_service_data

__all__ = [
    # Base provider
    'BaseSchemaOrgProvider',
    'create_faker_with_base',
    
    # Person
    'SchemaOrgPersonProvider',
    'create_person_data',
    
    # Organization
    'SchemaOrgOrganizationProvider',
    'create_organization_data',
    
    # BankAccount
    'SchemaOrgBankAccountProvider',
    'create_bank_account_data',
    
    # Order
    'SchemaOrgOrderProvider',
    'create_order_data',
    
    # Product
    'SchemaOrgProductProvider',
    'create_product_data',
    
    # Place
    'SchemaOrgPlaceProvider',
    'create_place_data',
    
    # Event
    'SchemaOrgEventProvider',
    'create_event_data',
    
    # Offer
    'SchemaOrgOfferProvider',
    'create_offer_data',
    
    # Review
    'SchemaOrgReviewProvider',
    'create_review_data',
    'create_aggregate_rating_data',
    
    # LocalBusiness
    'SchemaOrgLocalBusinessProvider',
    'create_local_business_data',
    
    # Course
    'SchemaOrgCourseProvider',
    'create_course_data',
    
    # JobPosting
    'SchemaOrgJobPostingProvider',
    'create_job_posting_data',
    
    # Article
    'SchemaOrgArticleProvider',
    'create_article_data',
    
    # Book
    'SchemaOrgBookProvider',
    'create_book_data',
    
    # Invoice
    'SchemaOrgInvoiceProvider',
    'create_invoice_data',
    
    # Restaurant
    'SchemaOrgRestaurantProvider',
    'create_restaurant_data',
    
    # Hotel
    'SchemaOrgHotelProvider',
    'create_hotel_data',
    
    # SoftwareApplication
    'SchemaOrgSoftwareApplicationProvider',
    'create_software_application_data',
    
    # Recipe
    'SchemaOrgRecipeProvider',
    'create_recipe_data',
    
    # FinancialProduct
    'SchemaOrgFinancialProductProvider',
    'create_financial_product_data',
    
    # DepositAccount
    'SchemaOrgDepositAccountProvider',
    'create_deposit_account_data',
    
    # CurrencyConversionService
    'SchemaOrgCurrencyConversionServiceProvider',
    'create_currency_conversion_service_data',
    
    # InvestmentOrDeposit
    'SchemaOrgInvestmentOrDepositProvider',
    'create_investment_or_deposit_data',
    
    # BrokerageAccount
    'SchemaOrgBrokerageAccountProvider',
    'create_brokerage_account_data',
    
    # InvestmentFund
    'SchemaOrgInvestmentFundProvider',
    'create_investment_fund_data',
    
    # LoanOrCredit
    'SchemaOrgLoanOrCreditProvider',
    'create_loan_or_credit_data',
    
    # CreditCard
    'SchemaOrgCreditCardProvider',
    'create_credit_card_data',
    
    # MortgageLoan
    'SchemaOrgMortgageLoanProvider',
    'create_mortgage_loan_data',
    
    # PaymentCard
    'SchemaOrgPaymentCardProvider',
    'create_payment_card_data',
    
    # PaymentService
    'SchemaOrgPaymentServiceProvider',
    'create_payment_service_data',
]

