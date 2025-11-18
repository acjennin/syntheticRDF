"""
Custom Faker provider for Schema.org/Book properties.
Generates realistic data for books including library catalogs and bookstores.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime
import random


class SchemaOrgBookProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Book properties."""
    
    # Book-specific data
    BOOK_FORMATS = [
        "Hardcover", "Paperback", "EBook", "AudiobookFormat", "GraphicNovel"
    ]
    
    GENRES = [
        "Fiction", "Non-Fiction", "Mystery", "Science Fiction", "Fantasy",
        "Romance", "Thriller", "Horror", "Biography", "History",
        "Science", "Philosophy", "Self-Help", "Business", "Cooking"
    ]
    
    def book_name(self):
        """Book title."""
        adjectives = self.fake.words(nb=2)
        nouns = self.fake.words(nb=1)
        return f"{' '.join(adjectives).title()}: {nouns[0].title()}"
    
    def book_description(self):
        """Book description."""
        return self.common_description()
    
    def book_isbn(self):
        """International Standard Book Number."""
        # Generate 13-digit ISBN-13 format
        prefix = "978"
        group = str(random.randint(0, 9))
        publisher = str(random.randint(10000, 99999))
        title = str(random.randint(100, 999))
        # Calculate check digit (simplified - just use random)
        check = str(random.randint(0, 9))
        return f"{prefix}-{group}-{publisher}-{title}-{check}"
    
    def book_book_format(self):
        """Format of the book."""
        return random.choice(self.BOOK_FORMATS)
    
    def book_author(self):
        """Book author name."""
        return self.fake.name()
    
    def book_publisher(self):
        """Book publisher."""
        publishers = [
            "Penguin Random House", "HarperCollins", "Simon & Schuster",
            "Macmillan Publishers", "Hachette Book Group", "Scholastic",
            "Oxford University Press", "Cambridge University Press"
        ]
        return random.choice(publishers)
    
    def book_number_of_pages(self):
        """Number of pages."""
        return random.randint(100, 800)
    
    def book_date_published(self):
        """Date book was published."""
        return self.common_date(start_year=1950, end_year=2024)
    
    def book_illustrator(self):
        """Book illustrator."""
        return self.fake.name()
    
    def book_translator(self):
        """Book translator."""
        return self.fake.name()
    
    def book_genre(self):
        """Book genre."""
        return random.choice(self.GENRES)
    
    def book_aggregate_rating(self):
        """Book aggregate rating."""
        return round(random.uniform(3.0, 5.0), 1)
    
    def book_review_count(self):
        """Number of book reviews."""
        return random.randint(5, 1000)
    
    def book_image_url(self):
        """Book cover image URL."""
        book_name = self.book_name().lower().replace(" ", "-").replace(":", "")
        return f"https://example.com/images/books/{book_name}.jpg"
    
    def book_language(self):
        """Language of the book."""
        languages = ["English", "Spanish", "French", "German", "Italian", "Portuguese"]
        return random.choice(languages)
    
    def book_edition(self):
        """Book edition."""
        editions = ["First Edition", "Second Edition", "Third Edition", "Revised Edition"]
        return random.choice(editions)


def create_book_data(num_entities=10, seed=None):
    """
    Generate book data using the custom provider.
    
    Args:
        num_entities: Number of book entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing book data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgBookProvider)
    
    books = []
    
    for i in range(num_entities):
        book = {
            "@type": "Book",
            "name": fake.book_name(),
            "description": fake.book_description(),
        }
        
        # Optional properties
        if random.random() < 0.9:
            book["isbn"] = fake.book_isbn()
        
        if random.random() < 0.8:
            book["bookFormat"] = fake.book_book_format()
        
        if random.random() < 0.9:
            book["author"] = fake.book_author()
        
        if random.random() < 0.8:
            book["publisher"] = fake.book_publisher()
        
        if random.random() < 0.7:
            book["numberOfPages"] = fake.book_number_of_pages()
        
        if random.random() < 0.8:
            book["datePublished"] = fake.book_date_published()
        
        if random.random() < 0.3:
            book["illustrator"] = fake.book_illustrator()
        
        if random.random() < 0.2:
            book["translator"] = fake.book_translator()
        
        if random.random() < 0.7:
            book["genre"] = fake.book_genre()
        
        # Ratings
        if random.random() < 0.6:
            rating = fake.book_aggregate_rating()
            review_count = fake.book_review_count()
            book["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        if random.random() < 0.8:
            book["image"] = fake.book_image_url()
        
        if random.random() < 0.6:
            book["inLanguage"] = fake.book_language()
        
        if random.random() < 0.4:
            book["bookEdition"] = fake.book_edition()
        
        books.append(book)
    
    return books


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Book Provider\n")
    print("=" * 80)
    
    books = create_book_data(num_entities=3, seed=42)
    
    for i, book in enumerate(books, 1):
        print(f"\nBook {i}:")
        print("-" * 80)
        for key, value in book.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

