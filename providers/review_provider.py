"""
Custom Faker provider for Schema.org/Review properties.
Generates realistic data for reviews and ratings of products, organizations, and services.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgReviewProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Review properties."""
    
    # Review-specific data
    REVIEW_TYPES = [
        "Review", "AggregateRating", "Rating"
    ]
    
    def review_author(self):
        """Review author name."""
        return self.fake.name()
    
    def review_date_published(self):
        """Date the review was published."""
        past_date = datetime.now() - timedelta(days=random.randint(1, 730))
        return past_date.isoformat()
    
    def review_body(self):
        """Review text content."""
        # Generate realistic review text
        review_templates = [
            "This is a great product! I've been using it for a while now and I'm very satisfied.",
            "Excellent quality and fast shipping. Highly recommend!",
            "Good value for money. Does what it's supposed to do.",
            "Not bad, but could be better. Some features are missing.",
            "Disappointed with this purchase. Quality is not what I expected.",
            "Amazing service! The staff was very helpful and professional.",
            "Great experience overall. Will definitely come back.",
            "Average quality. Nothing special but gets the job done.",
            "Outstanding! Exceeded my expectations in every way.",
            "Poor quality. Would not recommend to others."
        ]
        return random.choice(review_templates)
    
    def review_rating_value(self):
        """Rating value (1-5 stars typically)."""
        # Weighted towards positive ratings (realistic distribution)
        weights = [0.05, 0.10, 0.15, 0.30, 0.40]  # 1-5 stars
        ratings = [1, 2, 3, 4, 5]
        return random.choices(ratings, weights=weights)[0]
    
    def review_best_rating(self):
        """Best possible rating value."""
        return 5
    
    def review_worst_rating(self):
        """Worst possible rating value."""
        return 1
    
    def review_item_reviewed(self):
        """Item being reviewed (product name, organization name, etc.)."""
        return self.fake.company()
    
    def review_publisher(self):
        """Publisher of the review."""
        return self.fake.company()
    
    def review_headline(self):
        """Review headline."""
        headlines = [
            "Great product!",
            "Highly recommended",
            "Good value",
            "Not impressed",
            "Excellent service",
            "Could be better",
            "Amazing quality",
            "Disappointing",
            "Worth the price",
            "Average at best"
        ]
        return random.choice(headlines)
    
    def review_positive_notes(self):
        """Positive aspects mentioned."""
        positives = [
            "Fast shipping", "Good quality", "Great customer service",
            "Easy to use", "Good value", "Reliable", "Well designed",
            "Durable", "Affordable", "Professional"
        ]
        return random.sample(positives, random.randint(1, 3))
    
    def review_negative_notes(self):
        """Negative aspects mentioned."""
        negatives = [
            "Slow shipping", "Poor quality", "Bad customer service",
            "Hard to use", "Overpriced", "Unreliable", "Poor design",
            "Breaks easily", "Expensive", "Unprofessional"
        ]
        return random.sample(negatives, random.randint(0, 2))


def create_review_data(num_entities=10, seed=None):
    """
    Generate review data using the custom provider.
    
    Args:
        num_entities: Number of review entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing review data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgReviewProvider)
    
    reviews = []
    
    for i in range(num_entities):
        rating_value = fake.review_rating_value()
        
        review = {
            "@type": "Review",
            "author": fake.review_author(),
            "datePublished": fake.review_date_published(),
            "reviewBody": fake.review_body(),
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": rating_value,
                "bestRating": fake.review_best_rating(),
                "worstRating": fake.review_worst_rating()
            },
        }
        
        # Optional properties
        if random.random() < 0.7:
            review["headline"] = fake.review_headline()
        
        if random.random() < 0.9:
            review["itemReviewed"] = fake.review_item_reviewed()
        
        if random.random() < 0.6:
            review["publisher"] = fake.review_publisher()
        
        reviews.append(review)
    
    return reviews


def create_aggregate_rating_data(num_entities=10, seed=None):
    """
    Generate aggregate rating data (summary of multiple reviews).
    
    Args:
        num_entities: Number of aggregate rating entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing aggregate rating data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgReviewProvider)
    
    ratings = []
    
    for i in range(num_entities):
        # Aggregate rating is typically between 3.0 and 5.0
        rating_value = round(random.uniform(3.0, 5.0), 1)
        review_count = random.randint(5, 500)
        
        rating = {
            "@type": "AggregateRating",
            "ratingValue": rating_value,
            "bestRating": 5,
            "worstRating": 1,
            "reviewCount": review_count
        }
        
        ratings.append(rating)
    
    return ratings


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Review Provider\n")
    print("=" * 80)
    
    reviews = create_review_data(num_entities=3, seed=42)
    
    for i, review in enumerate(reviews, 1):
        print(f"\nReview {i}:")
        print("-" * 80)
        for key, value in review.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

