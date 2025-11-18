"""
Custom Faker provider for Schema.org/Event properties.
Generates realistic data for events including conferences, concerts, and meetings.
"""

from faker import Faker
from faker.providers import BaseProvider
from .base_provider import BaseSchemaOrgProvider
from datetime import datetime, timedelta
import random


class SchemaOrgEventProvider(BaseSchemaOrgProvider):
    """Provider for Schema.org/Event properties."""
    
    # Event-specific data
    EVENT_TYPES = [
        "BusinessEvent", "ChildrensEvent", "ComedyEvent", "CourseInstance",
        "DanceEvent", "DeliveryEvent", "EducationEvent", "EventSeries",
        "ExhibitionEvent", "Festival", "FoodEvent", "LiteraryEvent",
        "MusicEvent", "PublicationEvent", "SaleEvent", "ScreeningEvent",
        "SocialEvent", "SportsEvent", "TheaterEvent", "VisualArtsEvent"
    ]
    
    EVENT_STATUSES = [
        "EventScheduled",
        "EventCancelled",
        "EventPostponed",
        "EventRescheduled"
    ]
    
    ATTENDANCE_MODES = [
        "OfflineEventAttendanceMode",
        "OnlineEventAttendanceMode",
        "MixedEventAttendanceMode"
    ]
    
    def event_name(self):
        """Event name."""
        event_types = [
            "Conference", "Concert", "Workshop", "Seminar", "Festival",
            "Exhibition", "Convention", "Summit", "Symposium", "Meetup",
            "Webinar", "Training", "Show", "Gala", "Awards"
        ]
        topics = [
            "Technology", "Business", "Music", "Art", "Science",
            "Education", "Healthcare", "Finance", "Marketing", "Design"
        ]
        return f"{random.choice(event_types)} on {random.choice(topics)}"
    
    def event_description(self):
        """Event description."""
        return self.common_description()
    
    def event_start_date(self):
        """Event start date."""
        start_date = datetime.now() + timedelta(days=random.randint(1, 365))
        return start_date.isoformat()
    
    def event_end_date(self, start_date_str=None):
        """Event end date."""
        if start_date_str:
            try:
                start_date = datetime.fromisoformat(start_date_str)
                # Event lasts 1-7 days
                duration_days = random.randint(1, 7)
                end_date = start_date + timedelta(days=duration_days)
                return end_date.isoformat()
            except:
                pass
        
        # Fallback
        start_date = datetime.now() + timedelta(days=random.randint(1, 365))
        end_date = start_date + timedelta(days=random.randint(1, 7))
        return end_date.isoformat()
    
    def event_duration(self):
        """Event duration in ISO 8601 format."""
        durations = ["PT1H", "PT2H", "PT3H", "PT4H", "PT8H", "P1D", "P2D", "P3D"]
        return random.choice(durations)
    
    def event_status(self):
        """Event status."""
        return random.choice(self.EVENT_STATUSES)
    
    def event_attendance_mode(self):
        """Event attendance mode."""
        return random.choice(self.ATTENDANCE_MODES)
    
    def event_location_name(self):
        """Event location name."""
        return self.fake.company() + " " + random.choice(["Hall", "Center", "Arena", "Theater", "Venue"])
    
    def event_organizer(self):
        """Event organizer name."""
        return self.fake.company()
    
    def event_performer(self):
        """Event performer name."""
        return self.fake.name()
    
    def event_sponsor(self):
        """Event sponsor name."""
        return self.fake.company()
    
    def event_maximum_attendee_capacity(self):
        """Maximum number of attendees."""
        capacities = [50, 100, 200, 500, 1000, 2000, 5000, 10000]
        return random.choice(capacities)
    
    def event_offers_price(self):
        """Ticket price."""
        prices = [0, 25, 50, 75, 100, 150, 200, 300, 500]
        return random.choice(prices)
    
    def event_offers_currency(self):
        """Ticket price currency."""
        return self.common_currency_code()
    
    def event_offers_availability(self):
        """Ticket availability."""
        availabilities = [
            "InStock",
            "SoldOut",
            "PreOrder",
            "LimitedAvailability"
        ]
        return random.choice(availabilities)
    
    def event_image_url(self):
        """Event image URL."""
        event_name = self.event_name().lower().replace(" ", "-")
        return f"https://example.com/images/events/{event_name}.jpg"
    
    def event_keywords(self):
        """Event keywords."""
        keywords = self.fake.words(nb=random.randint(3, 6))
        return ", ".join(keywords)


def create_event_data(num_entities=10, seed=None):
    """
    Generate event data using the custom provider.
    
    Args:
        num_entities: Number of event entities to generate
        seed: Random seed for reproducibility
    
    Returns:
        List of dictionaries containing event data
    """
    if seed is not None:
        Faker.seed(seed)
        random.seed(seed)
    
    fake = Faker()
    fake.add_provider(SchemaOrgEventProvider)
    
    events = []
    
    for i in range(num_entities):
        start_date = fake.event_start_date()
        end_date = fake.event_end_date(start_date)
        
        event = {
            "@type": "Event",
            "name": fake.event_name(),
            "description": fake.event_description(),
            "startDate": start_date,
            "endDate": end_date,
        }
        
        # Optional properties
        if random.random() < 0.7:
            event["duration"] = fake.event_duration()
        
        event["eventStatus"] = fake.event_status()
        
        if random.random() < 0.8:
            event["eventAttendanceMode"] = fake.event_attendance_mode()
        
        # Location
        if random.random() < 0.9:
            event["location"] = {
                "name": fake.event_location_name(),
                "address": fake.common_address()
            }
        
        # Organizer
        if random.random() < 0.8:
            event["organizer"] = fake.event_organizer()
        
        # Performers
        if random.random() < 0.5:
            num_performers = random.randint(1, 3)
            event["performer"] = [fake.event_performer() for _ in range(num_performers)]
        
        # Sponsor
        if random.random() < 0.4:
            event["sponsor"] = fake.event_sponsor()
        
        # Capacity
        if random.random() < 0.6:
            event["maximumAttendeeCapacity"] = fake.event_maximum_attendee_capacity()
        
        # Offers (tickets)
        if random.random() < 0.7:
            price = fake.event_offers_price()
            event["offers"] = {
                "price": price,
                "priceCurrency": fake.event_offers_currency(),
                "availability": fake.event_offers_availability(),
                "url": fake.common_url()
            }
        
        # Image
        if random.random() < 0.6:
            event["image"] = fake.event_image_url()
        
        # Keywords
        if random.random() < 0.5:
            event["keywords"] = fake.event_keywords()
        
        events.append(event)
    
    return events


if __name__ == "__main__":
    # Test the provider
    print("Testing Schema.org Event Provider\n")
    print("=" * 80)
    
    events = create_event_data(num_entities=3, seed=42)
    
    for i, event in enumerate(events, 1):
        print(f"\nEvent {i}:")
        print("-" * 80)
        for key, value in event.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for k, v in value.items():
                    print(f"    {k}: {v}")
            elif isinstance(value, list):
                print(f"  {key}:")
                for item in value:
                    print(f"    - {item}")
            else:
                print(f"  {key}: {value}")

