from scrape_result import ScrapeResult


def childrens(driver):
    url = 'https://mychartos.seattlechildrens.org/mychart/SignupAndSchedule/' \
                'EmbeddedSchedule?id=600927&dept=200204&vt=2485&lang=en-US'

    driver.get(url)

    slots = driver.find_elements_by_class_name('slotdetailaction')
    # for el in slots:
    #     print(el.get_attribute('innerHTML'))
    num_appointments = len(slots)
    return ScrapeResult("Seattle Children's Hospital", url, num_appointments > 0,
                        '4800 Sand Point Way NE Seattle, WA', 98105, num_appointments)
