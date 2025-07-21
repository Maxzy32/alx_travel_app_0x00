import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2),
                is_available=random.choice([True, False])
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with listings.'))
