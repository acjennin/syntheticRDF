"""
Custom Faker provider for Schema.org/Course properties.
Generates realistic data for educational courses and training programs.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgCourseProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Course properties."""
    
    # Course-specific data
    COURSE_CATEGORIES = [
        "Computer Science", "Business", "Mathematics", "Science",
        "Engineering", "Arts", "Languages", "History", "Philosophy",
        "Psychology", "Medicine", "Law", "Education", "Marketing",
        "Finance", "Design", "Photography", "Music", "Writing"
    ]
    
    COURSE_MODES = [
        "Online", "OnSite", "Blended", "Mixed"
    ]
    
    EDUCATIONAL_LEVELS = [
        "Beginner", "Intermediate", "Advanced", "Expert"
    ]
    
    CREDENTIALS = [
        "Certificate", "Diploma", "Degree", "Professional Certificate",
        "Micro-credential", "Badge"
    ]
    
    def course_name(self):
        """Course name."""
        category = random.choice(self.COURSE_CATEGORIES)
        levels = ["Introduction to", "Advanced", "Fundamentals of", "Mastering"]
        return f"{random.choice(levels)} {category}"
    
    def course_description(self):
        """Course description."""
        return self.common_description()
    
    def course_code(self):
        """Course code/identifier."""
        prefix = random.choice(["CS", "BUS", "MATH", "ENG", "ART", "SCI"])
        number = random.randint(100, 999)
        return f"{prefix}{number}"
    
    def course_provider(self):
        """Course provider (educational organization)."""
        return self.fake.company() + " " + random.choice(["University", "College", "Academy", "Institute"])
    
    def course_instructor(self):
        """Course instructor name."""
        return self.fake.name()
    
    def course_prerequisites(self):
        """Course prerequisites."""
        prerequisites = [
            "Basic knowledge of programming",
            "High school diploma",
            "Previous course completion",
            "Work experience in the field",
            "No prerequisites required"
        ]
        return random.choice(prerequisites)
    
    def course_educational_level(self):
        """Educational level of the course."""
        return random.choice(self.EDUCATIONAL_LEVELS)
    
    def course_credential_awarded(self):
        """Credential awarded upon completion."""
        return random.choice(self.CREDENTIALS)
    
    def course_time_required(self):
        """Time required to complete the course."""
        durations = ["PT10H", "PT20H", "PT40H", "PT80H", "P4W", "P8W", "P12W", "P16W"]
        return random.choice(durations)
    
    def course_teaches(self):
        """What the course teaches."""
        skills = [
            "Programming fundamentals", "Data analysis", "Web development",
            "Business strategy", "Marketing techniques", "Design principles",
            "Communication skills", "Problem solving", "Critical thinking"
        ]
        return random.choice(skills)
    
    def course_aggregate_rating(self):
        """Course aggregate rating."""
        return round(random.uniform(3.5, 5.0), 1)
    
    def course_review_count(self):
        """Number of course reviews."""
        return random.randint(10, 500)
    
    def course_number_of_credits(self):
        """Number of credits awarded."""
        return random.randint(1, 6)
    
    def course_start_date(self):
        """Course start date."""
        future_date = datetime.now() + timedelta(days=random.randint(1, 180))
        return future_date.isoformat()
    
    def course_end_date(self, start_date_str=None):
        """Course end date."""
        if start_date_str:
            try:
                start_date = datetime.fromisoformat(start_date_str)
                # Course lasts 4-16 weeks
                duration_weeks = random.randint(4, 16)
                end_date = start_date + timedelta(weeks=duration_weeks)
                return end_date.isoformat()
            except:
                pass
        
        # Fallback
        start_date = datetime.now() + timedelta(days=random.randint(1, 180))
        end_date = start_date + timedelta(weeks=random.randint(4, 16))
        return end_date.isoformat()


def create_course_data(num_entities=10, seed=None):
    """
    Generate course data using the custom provider.
    
    Args:
        num_entities: Number of course entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing course data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgCourseProvider)
    
    courses = []
    
    for i in range(num_entities):
        start_date = fake.course_start_date()
        end_date = fake.course_end_date(start_date)
        
        course = {
            "@type": "Course",
            "name": fake.course_name(),
            "description": fake.course_description(),
            "courseCode": fake.course_code(),
        }
        
        # Optional properties
        if random.random() < 0.9:
            course["provider"] = fake.course_provider()
        
        if random.random() < 0.8:
            course["instructor"] = fake.course_instructor()
        
        if random.random() < 0.6:
            course["coursePrerequisites"] = fake.course_prerequisites()
        
        if random.random() < 0.7:
            course["educationalLevel"] = fake.course_educational_level()
        
        if random.random() < 0.7:
            course["educationalCredentialAwarded"] = fake.course_credential_awarded()
        
        if random.random() < 0.8:
            course["timeRequired"] = fake.course_time_required()
        
        if random.random() < 0.7:
            course["teaches"] = fake.course_teaches()
        
        # Dates
        if random.random() < 0.6:
            course["startDate"] = start_date
            course["endDate"] = end_date
        
        # Ratings
        if random.random() < 0.6:
            rating = fake.course_aggregate_rating()
            review_count = fake.course_review_count()
            course["aggregateRating"] = {
                "ratingValue": rating,
                "bestRating": 5,
                "worstRating": 1,
                "reviewCount": review_count
            }
        
        # Credits
        if random.random() < 0.5:
            course["numberOfCredits"] = fake.course_number_of_credits()
        
        courses.append(course)
    
    return courses


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Course Provider\n")
    print("=" * 80)
    
    courses = create_course_data(num_entities=3, seed=42)
    
    for i, course in enumerate(courses, 1):
        print(f"\nCourse {i}:")
        print("-" * 80)
        for key, value in course.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            else:
                print(f"  {key}: {value}")

