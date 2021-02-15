from .helpers import try_every_second
from scrape_result import ScrapeResult  # type: ignore
from selenium import webdriver


def seattle_vna():
    url = "https://schedule.seattlevna.com/home"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    def get_availability():
        html = driver.find_element_by_class_name('section__container').get_attribute('innerHTML')
        if html.find('loader') != -1:  # If loading
            raise Exception("not done loading")  # Will be caught
        print(html)
        return html.find('No sites available') == -1

    available = try_every_second(get_availability)

    driver.close()
    return ScrapeResult('Seattle Visiting Nurse Association', url, available,
                        '170 W Dayton St Suite 103A, Edmonds, WA', 98020)
