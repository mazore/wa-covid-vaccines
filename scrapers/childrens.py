from selenium import webdriver
from scrape_result import ScrapeResult


def childrens():
    chart_url = 'https://mychartos.seattlechildrens.org/mychart/SignupAndSchedule/' \
                'EmbeddedSchedule?id=600927&dept=200204&vt=2485&lang=en-US'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(chart_url)
    slots = driver.find_elements_by_class_name('slotdetailaction')
    # for el in slots:
    #     print(el.get_attribute('innerHTML'))
    num_appointments = len(slots)
    return ScrapeResult("Seattle Children's Hospital", chart_url,
                        num_appointments > 0, num_appointments)


if __name__ == '__main__':
    childrens()
