import random
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Employee 

class Command(BaseCommand):
    help = 'Populate fake data into the database'

    def handle(self, *args, **options):
        fake = Faker()
        num_entries = 4
        for _ in range(num_entries):
            # Create fake data and save to the database
            fakedata = Employee (
              
                name = fake.name(),
    
                salary = fake.salary() ,
                address =  fake.address(),
                religion = fake.religion(),
                note = fake.note(),
              
                image = fake.image()
            )
            fakedata.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {num_entries} fake data entries'))