from selenium import webdriver


def sign_up_genius(url):
    """Returns True if all appointments are filled"""
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    num_filled = total = 0
    for i in range(2, 18):
        total += 1
        xpath = f'//*[@id="signupForm"]/div[2]/table/tbody/tr[{i}]/td[2]/table/tbody/tr/td[3]/div/span'
        el = driver.find_element_by_xpath(xpath)
        if el.get_attribute('innerHTML') == 'Already filled':
            num_filled += 1
    return num_filled == total
