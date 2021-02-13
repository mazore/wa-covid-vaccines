from firebase import firebase
from scrapers import all_scrapers  # type: ignore
from scrape_result import ScrapeResult  # type: ignore
from time import time

db = firebase.FirebaseApplication('https://covid-vaccines-default-rtdb.firebaseio.com/', None)

results = []
for scraper in all_scrapers:
    results.append(scraper())
    print('\nscraped ' + scraper.__name__)

for result in results:
    if type(result) == ScrapeResult:  # Other possibility is to return a list of ScrapeResults
        result = [result]  # Allow to iterate

    for scrape_result in result:
        for key, value in scrape_result.__dict__.items():
            db.put(f'scrapes/{scrape_result.name}', key, value)
        db.put(f'scrapes/{scrape_result.name}', 'time', time())
        if scrape_result.available:
            db.put(f'scrapes/{scrape_result.name}', 'last_appointment_time', time())
        print(f'available: {scrape_result.available}, at {scrape_result.name}')
