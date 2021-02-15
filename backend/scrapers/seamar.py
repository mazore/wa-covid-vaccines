from .helpers import children
from scrape_result import ScrapeResult  # type: ignore
from selenium import webdriver


def seamar():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRbT-9tFmezrnQ6ETYmF81PDcqgHg5e' \
          'DD4Xva8krr9GiELl9fFPMhuUvm5WH-qsU1jf-FEcSQKhVM10/pubhtml/sheet?headers=false&gid=0'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    availabilities = []
    for i in range(5, 38):
        # name = driver.find_element_by_xpath(f'//*[@id="0"]/div/table/tbody/tr[{i}]/td[1]')
        # children(name)[0].get_attribute('innerHTML')
        availability = driver.find_element_by_xpath(f'//*[@id="0"]/div/table/tbody/tr[{i}]/td[2]')
        availabilities.append(availability.get_attribute('innerHTML') != 'No Vaccines Available')

    driver.close()
    return ScrapeResult('Seamar', url, any(availabilities), 'Multiple sites', None)
