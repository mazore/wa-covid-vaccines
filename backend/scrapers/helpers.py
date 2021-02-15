from time import sleep


def children(element):
    return element.find_elements_by_xpath('./child::*')


def try_every_second(func, refresh_after=None, driver=None):
    i = 0
    while True:
        try:
            return func()
        except Exception as e:
            print(f'tried {func.__name__} and failed from {e}')
            i += 1
            if refresh_after is not None and i % refresh_after == 0:
                driver.refresh()
            sleep(1)
