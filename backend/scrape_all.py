from firebase import firebase
from scrapers import all_scrapers  # type: ignore
from scrapers import *  # type: ignore
from time import time

db = firebase.FirebaseApplication('https://covid-vaccines-default-rtdb.firebaseio.com/', None)

for result in [scraper() for scraper in all_scrapers]:
    for key, value in result.__dict__.items():
        db.put(f'scrapes/{result.name}', key, value)
    db.put(f'scrapes/{result.name}', 'time', time())
    if result.available:
        db.put(f'scrapes/{result.name}', 'last_appointment_time', time())
    print(f'available: {result.available}, at {result.name}')
