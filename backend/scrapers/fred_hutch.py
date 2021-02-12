from selenium import webdriver
from time import sleep
from scrape_result import ScrapeResult  # type: ignore


def fred_hutch():
    url = "https://www.solvhealth.com/book-online/gJ8GYA"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.find_element_by_class_name('jss112').click()  # Yes button
    driver.find_element_by_class_name('jss112').click()  # Find Next Available Visit button

    el = driver.find_element_by_class_name('TabView__Content-sc-1oe0awg')
    c1 = el.find_elements_by_xpath('./child::*')[0]
    c2 = c1.find_elements_by_xpath('./child::*')[0]
    c3 = c2.find_elements_by_xpath('./child::*')[0]
    c4 = c3.find_elements_by_xpath('./child::*')[1]

    def get_is_available():
        row_container = c4.find_elements_by_xpath('./child::*')[0]
        for row in row_container.find_elements_by_xpath('./child::*'):
            for day in row.find_elements_by_xpath('./child::*'):
                if day.find_elements_by_xpath('./child::*')[0].get_attribute('tabindex') == "0":  # Button enabled
                    day.click()
                    sleep(2)
                    if el.get_attribute('innerHTML').find('No Visit Times Left') == -1:
                        return True
        return False

    if get_is_available():
        return ScrapeResult('Fred Hutch', url, True)

    # Page to next month
    header = c3.find_elements_by_xpath('./child::*')[0]
    header = header.find_elements_by_xpath('./child::*')[0]
    header.find_elements_by_xpath('./child::*')[2].click()
    return ScrapeResult('Fred Hutch', url, get_is_available())
