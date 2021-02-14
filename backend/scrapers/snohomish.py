from .sign_up_genius import sign_up_genius
from scrape_result import ScrapeResult  # type: ignore
from selenium import webdriver
from time import sleep


def snohomish():
    url = 'https://snohomish-county-coronavirus-response-snoco-gis.hub.arcgis.com/pages/covid-19-vaccine'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    sleep(3)

    url1 = driver.find_element_by_xpath('//*[@id="ember87"]/h6[2]/ul[2]/li/a').get_attribute('innerHTML')
    url2 = driver.find_element_by_xpath('//*[@id="ember87"]/h6[2]/ul[3]/li/a').get_attribute('innerHTML')

    if not url1.startswith('https://'):
        url1 = 'https://' + url1
    if not url2.startswith('https://'):
        url2 = 'https://' + url2

    return [ScrapeResult("Monroe", url1, not sign_up_genius(url1), '13850 179th Ave SE Monroe WA', 98272),
            ScrapeResult("Arlington", url2, not sign_up_genius(url2), '4226 188th St NE Arlington WA', 98223)]
