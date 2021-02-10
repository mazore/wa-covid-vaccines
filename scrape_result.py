from time import time


class ScrapeResult:
    def __init__(self, url, available, num_appointments=None):
        """
        url - link to website

        available - boolean whether appointments are available

        num_appointments (optional) - number of appointments available

        time = unix time of update

        To add:
        - appointment times
        - vaccine type (Moderna or Pfizer)
        - address
        - eligibility
        """
        self.url = url
        self.available = available
        self.num_appointments = num_appointments
        self.time = time()

    def __repr__(self):
        return 'url: {url}\n' \
               'available: {available}\n' \
               'num_appointments: {num_appointments}\n' \
               'time: {time}'.format(**self.__dict__)
