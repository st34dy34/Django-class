from django.core.management.base import BaseCommand
from lekce3.models import Car  # Nahraď 'myapp' názvem své aplikace

class Command(BaseCommand):
    help = 'Vypíše všechna auta uložená v databázi'

    def handle(self, *args, **kwargs):
        cars = Car.objects.all()
        if cars.exists():
            for car in cars:
                self.stdout.write(f'Značka: {car.brand}, Barva: {car.color}')
        else:
            self.stdout.write('V databázi nejsou žádná auta.')
