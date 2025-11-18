"""
Custom Faker provider for Schema.org/Article properties.
Generates realistic data for articles including news, blog posts, and content.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgArticleProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Article properties."""
    
    # Article-specific data
    ARTICLE_SECTIONS = [
        "Technology", "Business", "Science", "Health", "Politics",
        "Sports", "Entertainment", "Lifestyle", "Education", "Finance",
        "Travel", "Food", "Fashion", "Opinion", "News"
    ]
    
    ARTICLE_TYPES = [
        "Article", "NewsArticle", "BlogPosting", "ScholarlyArticle",
        "TechArticle", "Report", "SocialMediaPosting"
    ]
    
    def article_headline(self):
        """Article headline."""
        topics = [
            "Breakthrough", "Analysis", "Report", "Study", "Review",
            "Guide", "Tutorial", "News", "Update", "Insight"
        ]
        subjects = [
            "Technology", "Business", "Science", "Health", "Market",
            "Industry", "Innovation", "Trends", "Development"
        ]
        return f"{random.choice(topics)}: {random.choice(subjects)}"
    
    def article_description(self):
        """Article description/abstract."""
        return self.common_description()
    
    def article_body(self):
        """Article body text."""
        # Generate longer text for article body
        paragraphs = random.randint(3, 8)
        text = ""
        for _ in range(paragraphs):
            text += self.fake.paragraph(nb_sentences=random.randint(3, 7)) + "\n\n"
        return text.strip()
    
    def article_article_section(self):
        """Article section/category."""
        return random.choice(self.ARTICLE_SECTIONS)
    
    def article_author(self):
        """Article author name."""
        return self.fake.name()
    
    def article_publisher(self):
        """Article publisher (organization)."""
        return self.fake.company()
    
    def article_date_published(self):
        """Date article was published."""
        past_date = datetime.now() - timedelta(days=random.randint(0, 730))
        return past_date.isoformat()
    
    def article_date_modified(self, published_date_str=None):
        """Date article was last modified."""
        if published_date_str:
            try:
                published_date = datetime.fromisoformat(published_date_str)
                modified_date = published_date + timedelta(days=random.randint(0, 30))
                return modified_date.isoformat()
            except:
                pass
        
        # Fallback
        past_date = datetime.now() - timedelta(days=random.randint(0, 700))
        return past_date.isoformat()
    
    def article_word_count(self):
        """Word count of the article."""
        return random.randint(500, 5000)
    
    def article_keywords(self):
        """Article keywords."""
        keywords = self.fake.words(nb=random.randint(5, 10))
        return ", ".join(keywords)
    
    def article_image_url(self):
        """Article image URL."""
        headline = self.article_headline().lower().replace(" ", "-").replace(":", "")
        return f"https://example.com/images/articles/{headline}.jpg"
    
    def article_url(self):
        """URL to the article."""
        headline = self.article_headline().lower().replace(" ", "-").replace(":", "")
        return f"https://example.com/articles/{headline}"
    
    def article_about(self):
        """Subject matter of the article."""
        topics = [
            "Technology trends", "Business strategy", "Scientific research",
            "Health and wellness", "Market analysis", "Industry insights"
        ]
        return random.choice(topics)
    
    def article_in_language(self):
        """Language of the article."""
        languages = ["en", "es", "fr", "de", "it", "pt", "zh", "ja"]
        return random.choice(languages)


def create_article_data(num_entities=10, seed=None):
    """
    Generate article data using the custom provider.
    
    Args:
        num_entities: Number of article entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing article data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgArticleProvider)
    
    articles = []
    
    for i in range(num_entities):
        published_date = fake.article_date_published()
        modified_date = fake.article_date_modified(published_date)
        
        article = {
            "@type": "Article",
            "headline": fake.article_headline(),
            "description": fake.article_description(),
            "articleBody": fake.article_body(),
        }
        
        # Optional properties
        article["articleSection"] = fake.article_article_section()
        
        if random.random() < 0.9:
            article["author"] = fake.article_author()
        
        if random.random() < 0.8:
            article["publisher"] = fake.article_publisher()
        
        article["datePublished"] = published_date
        
        if random.random() < 0.6:
            article["dateModified"] = modified_date
        
        if random.random() < 0.7:
            article["wordCount"] = fake.article_word_count()
        
        if random.random() < 0.8:
            article["keywords"] = fake.article_keywords()
        
        if random.random() < 0.9:
            article["image"] = fake.article_image_url()
        
        if random.random() < 0.8:
            article["url"] = fake.article_url()
        
        if random.random() < 0.6:
            article["about"] = fake.article_about()
        
        if random.random() < 0.5:
            article["inLanguage"] = fake.article_in_language()
        
        articles.append(article)
    
    return articles


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Article Provider\n")
    print("=" * 80)
    
    articles = create_article_data(num_entities=3, seed=42)
    
    for i, article in enumerate(articles, 1):
        print(f"\nArticle {i}:")
        print("-" * 80)
        for key, value in article.items():
            if key == "articleBody":
                print(f"  {key}: {value[:100]}...")
            elif isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

