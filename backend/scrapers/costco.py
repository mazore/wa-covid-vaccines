from .helpers import try_every_second
from scrape_result import ScrapeResult


class Location:
    def __init__(self, code, e_id, name_suffix, address, zip):
        self.code = code
        self.e_id = e_id
        self.name_suffix = name_suffix
        self.address = address
        self.zip = zip


def costco(driver):
    # spell-checker: disable
    locations = [
        Location('ctx9xpqe', 4985, 'Clarkston', '301 FIFTH STREET CLARKSTON, WA', 99403),
        Location('ctxyd41v', 4989, 'Covington', '27520 COVINGTON WAY SE COVINGTON, WA', 98042),
        Location('ctx6gxv6', 5031, 'Federal Way', '35100 ENCHANTED PARKWAY S. Federal Way, WA', 98003),

        Location('ctxq8qyy', 5061, 'Issaquah', '1801 10TH AVE NORTHWEST ISSAQUAH, WA', 98027),
        Location('ctx5cjym', 5003, 'Kirkland', '8629 120TH AVE NE Kirkland, WA', 98033),
        Location('ctx9e07c', 4995, 'Redmond', '7725 188TH AVE NE Redmond, WA', 98052),

        Location('ctx5hetv', 4935, 'Seattle', '4401 FOURTH AVE S Seattle, WA', 98134),
        Location('ctxymp9s', 4997, 'Aurora', '1175 NORTH 205th STREET SEATTLE, WA', 98133),
        Location('ctx5myxq', 4975, 'Tukwila', '400 COSTCO DR Tukwila, WA', 98188),
    ]

    # spell-checker: enable
    return [one_location(driver, location) for location in locations]


def one_location(driver, location):
    url = f'https://book-costcopharmacy.appointment-plus.com/{location.code}/?&e_id={location.e_id}#/'

    driver.get(url)

    def click_get_started():
        driver.find_element_by_xpath('//*[@id="page-content"]/div/div[2]/div[3]/ul/li/a').click()

    try_every_second(click_get_started, refresh_after=3, driver=driver)

    def get_is_available():
        html = driver.find_element_by_class_name('date-time-container').get_attribute('innerHTML')
        if html.find('progressbar') != -1:  # If loading
            raise Exception("not done loading")  # Will be caught
        return html.find('We’re sorry, but there are not available times.') == -1

    available = try_every_second(get_is_available, refresh_after=5, driver=driver)

    print('\n'*3, available, location.name_suffix, '\n'*3)

    return ScrapeResult(f'Costco {location.name_suffix}', url, available,
                        location.address, location.zip)
