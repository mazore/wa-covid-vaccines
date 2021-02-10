from firebase import firebase
from scrapers import all_scrapers

db = firebase.FirebaseApplication('https://covid-vaccines-default-rtdb.firebaseio.com/', None)

for scrape_result in [scraper() for scraper in all_scrapers]:
    resp = db.post('/covid-vaccines-default-rtdb/test-table', scrape_result.__dict__)
    print('\n', resp)
