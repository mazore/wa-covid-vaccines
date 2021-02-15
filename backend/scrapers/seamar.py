from scrape_result import ScrapeResult


def seamar(driver):
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRbT-9tFmezrnQ6ETYmF81PDcqgHg5e' \
          'DD4Xva8krr9GiELl9fFPMhuUvm5WH-qsU1jf-FEcSQKhVM10/pubhtml/sheet?headers=false&gid=0'

    driver.get(url)

    availabilities = []
    for i in range(5, 38):
        # name = driver.find_element_by_xpath(f'//*[@id="0"]/div/table/tbody/tr[{i}]/td[1]')
        # children(name)[0].get_attribute('innerHTML')
        availability = driver.find_element_by_xpath(f'//*[@id="0"]/div/table/tbody/tr[{i}]/td[2]')
        availabilities.append(availability.get_attribute('innerHTML') != 'No Vaccines Available')

    return ScrapeResult('Seamar', url, any(availabilities), 'Multiple sites', '')
