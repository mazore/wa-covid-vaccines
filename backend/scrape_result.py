class ScrapeResult:
    def __init__(self, name, url, available, num_appointments=None):
        """
        name - the name of the location

        url - link to website

        available - boolean whether appointments are available

        num_appointments (optional) - number of appointments available

        To add:
        - appointment available times
        - vaccine type (Moderna or Pfizer)
        - address
        - eligibility
        """
        self.name = name
        self.url = url
        self.available = available
        self.num_appointments = num_appointments
