from selenium import webdriver
from time import sleep
from scrape_result import ScrapeResult  # type: ignore


def seattle_vna():
    url = "https://schedule.seattlevna.com/home"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(2)
    html = driver.execute_script('return document.documentElement.innerHTML;')
    available = html.find('No sites available') == -1
    return ScrapeResult('Seattle Visiting Nurse Association', url, available)
