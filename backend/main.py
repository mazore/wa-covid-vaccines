from datetime import datetime
from firebase import firebase
import os
import psutil
from scrape_result import ScrapeResult
from secret import auth
from selenium import webdriver
from time import time

from scrapers.childrens import childrens
from scrapers.costco import costco
from scrapers.fred_hutch import fred_hutch
from scrapers.seamar import seamar
from scrapers.seattle_vna import seattle_vna
from scrapers.snohomish import snohomish


def update_db():
    start_time = time()

    all_scrapers = [childrens, costco, seamar, seattle_vna, fred_hutch, snohomish]

    db = firebase.FirebaseApplication('https://covid-vaccines-default-rtdb.firebaseio.com/', auth)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    results = []
    for scraper in all_scrapers:
        results.append(scraper(driver))
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

    db.put('/', 'last_updated', datetime.now().strftime(r'%B %d at %I:%M %p').replace(' 0', ' '))

    driver.close()

    print(f'\ntook: {time() - start_time} seconds')
    print('used', psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 'MB')


update_db()
