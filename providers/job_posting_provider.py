"""
Custom Faker provider for Schema.org/JobPosting properties.
Generates realistic data for job postings and employment opportunities.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgJobPostingProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/JobPosting properties."""
    
    # JobPosting-specific data
    EMPLOYMENT_TYPES = [
        "FULL_TIME",
        "PART_TIME",
        "CONTRACTOR",
        "TEMPORARY",
        "INTERN",
        "VOLUNTEER",
        "PER_DIEM",
        "OTHER"
    ]
    
    JOB_TITLES = [
        "Software Engineer", "Data Analyst", "Marketing Manager",
        "Sales Representative", "Product Manager", "Designer",
        "Accountant", "HR Specialist", "Customer Service Representative",
        "Project Manager", "Business Analyst", "Operations Manager",
        "Developer", "Consultant", "Administrator"
    ]
    
    WORK_SCHEDULES = [
        "Monday to Friday", "Flexible", "Shift Work", "Weekends",
        "Evening Shift", "Night Shift", "On-Call"
    ]
    
    def job_posting_title(self):
        """Job title."""
        return random.choice(self.JOB_TITLES)
    
    def job_posting_description(self):
        """Job description."""
        return self.common_description()
    
    def job_posting_date_posted(self):
        """Date the job was posted."""
        past_date = datetime.now() - timedelta(days=random.randint(0, 90))
        return past_date.isoformat()
    
    def job_posting_valid_through(self):
        """Date until which the job posting is valid."""
        future_date = datetime.now() + timedelta(days=random.randint(7, 90))
        return future_date.isoformat()
    
    def job_posting_employment_type(self):
        """Type of employment."""
        return random.choice(self.EMPLOYMENT_TYPES)
    
    def job_posting_hiring_organization(self):
        """Organization hiring for this position."""
        return self.fake.company()
    
    def job_posting_job_location(self):
        """Location of the job."""
        return {
            "address": self.common_address()
        }
    
    def job_posting_base_salary(self):
        """Base salary."""
        # Salary ranges by employment type
        salary_ranges = {
            "FULL_TIME": (40000, 150000),
            "PART_TIME": (20000, 60000),
            "CONTRACTOR": (50000, 200000),
            "TEMPORARY": (25000, 70000),
            "INTERN": (15000, 40000),
            "VOLUNTEER": (0, 0)
        }
        emp_type = random.choice(self.EMPLOYMENT_TYPES)
        min_sal, max_sal = salary_ranges.get(emp_type, (30000, 100000))
        return round(random.uniform(min_sal, max_sal), 2)
    
    def job_posting_salary_currency(self):
        """Salary currency."""
        return self.common_currency_code()
    
    def job_posting_work_hours(self):
        """Work hours."""
        return random.choice(self.WORK_SCHEDULES)
    
    def job_posting_qualifications(self):
        """Required qualifications."""
        qualifications = [
            "Bachelor's degree required",
            "Master's degree preferred",
            "3+ years of experience",
            "Professional certification",
            "High school diploma or equivalent",
            "No formal education required"
        ]
        return random.choice(qualifications)
    
    def job_posting_skills(self):
        """Required skills."""
        skills = [
            "Communication", "Problem Solving", "Teamwork", "Leadership",
            "Technical Skills", "Analytical Thinking", "Project Management",
            "Customer Service", "Time Management", "Creativity"
        ]
        num_skills = random.randint(3, 6)
        return random.sample(skills, num_skills)
    
    def job_posting_benefits(self):
        """Job benefits."""
        benefits = [
            "Health Insurance", "Dental Insurance", "Vision Insurance",
            "401(k) Matching", "Paid Time Off", "Flexible Schedule",
            "Remote Work", "Professional Development", "Gym Membership"
        ]
        num_benefits = random.randint(2, 5)
        return random.sample(benefits, num_benefits)
    
    def job_posting_application_deadline(self):
        """Application deadline."""
        future_date = datetime.now() + timedelta(days=random.randint(7, 60))
        return future_date.isoformat()
    
    def job_posting_application_url(self):
        """URL to apply for the job."""
        return self.common_url()


def create_job_posting_data(num_entities=10, seed=None):
    """
    Generate job posting data using the custom provider.
    
    Args:
        num_entities: Number of job posting entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing job posting data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgJobPostingProvider)
    
    job_postings = []
    
    for i in range(num_entities):
        employment_type = fake.job_posting_employment_type()
        base_salary = fake.job_posting_base_salary()
        
        job_posting = {
            "@type": "JobPosting",
            "title": fake.job_posting_title(),
            "description": fake.job_posting_description(),
            "datePosted": fake.job_posting_date_posted(),
            "employmentType": employment_type,
        }
        
        # Optional properties
        if random.random() < 0.8:
            job_posting["validThrough"] = fake.job_posting_valid_through()
        
        if random.random() < 0.9:
            job_posting["hiringOrganization"] = fake.job_posting_hiring_organization()
        
        if random.random() < 0.9:
            job_posting["jobLocation"] = fake.job_posting_job_location()
        
        # Salary (skip for volunteer positions)
        if employment_type != "VOLUNTEER" and random.random() < 0.7:
            job_posting["baseSalary"] = {
                "value": base_salary,
                "currency": fake.job_posting_salary_currency(),
                "unitText": "YEAR"
            }
        
        if random.random() < 0.7:
            job_posting["workHours"] = fake.job_posting_work_hours()
        
        if random.random() < 0.8:
            job_posting["qualifications"] = fake.job_posting_qualifications()
        
        if random.random() < 0.7:
            job_posting["skills"] = fake.job_posting_skills()
        
        if random.random() < 0.6:
            job_posting["jobBenefits"] = fake.job_posting_benefits()
        
        if random.random() < 0.5:
            job_posting["applicationDeadline"] = fake.job_posting_application_deadline()
        
        if random.random() < 0.8:
            job_posting["applicationUrl"] = fake.job_posting_application_url()
        
        job_postings.append(job_posting)
    
    return job_postings


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org JobPosting Provider\n")
    print("=" * 80)
    
    job_postings = create_job_posting_data(num_entities=3, seed=42)
    
    for i, job_posting in enumerate(job_postings, 1):
        print(f"\nJobPosting {i}:")
        print("-" * 80)
        for key, value in job_posting.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    if isinstance(v, list):
                        print(f"    {k}: {', '.join(v)}")
                    else:
                        print(f"    {k}: {v}")
            elif isinstance(value, list):
                print(f"  {key}: {', '.join(value)}")
            else:
                print(f"  {key}: {value}")

