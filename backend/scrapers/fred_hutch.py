from .helpers import children
from scrape_result import ScrapeResult  # type: ignore
from selenium import webdriver
from time import sleep


def fred_hutch():
    url = "https://www.solvhealth.com/book-online/gJ8GYA"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.find_element_by_class_name('jss112').click()  # Yes button
    driver.find_element_by_class_name('jss112').click()  # Find Next Available Visit button

    el = driver.find_element_by_class_name('TabView__Content-sc-1oe0awg')
    c1 = children(el)[0]  # For some reason xpath doesn't work past this point
    c2 = children(c1)[0]
    c3 = children(c2)[0]
    c4 = children(c3)[1]

    def get_is_available():
        row_container = children(c4)[0]
        for row in children(row_container):
            for day in children(row):
                if children(day)[0].get_attribute('tabindex') == "0":  # Button enabled
                    day.click()
                    sleep(2)
                    if el.get_attribute('innerHTML').find('No Visit Times Left') == -1:
                        return True
        return False

    if get_is_available():
        return ScrapeResult('Fred Hutch', url, True)

    # Page to next month
    header = children(c3)[0]
    header = children(header)[0]
    children(header)[2].click()
    available = get_is_available()
    driver.close()
    return ScrapeResult('Fred Hutch', url, available,
                        '1100 Fairview Ave N Seattle, WA', 98109)
