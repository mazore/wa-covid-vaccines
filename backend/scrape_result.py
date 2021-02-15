class ScrapeResult:
    def __init__(self, name, url, available, address, zip, num_appointments=None):
        """
        name: str - the name of the location

        url: str - link to website

        available: boolean - whether appointments are available

        address: str - address of site

        zip: int - zip code

        num_appointments (optional): int - number of appointments available

        To add:
        - appointment available times
        - vaccine type (Moderna or Pfizer)
        - eligibility
        """
        self.name = name
        self.url = url
        self.available = available
        self.address = address
        self.zip = zip
        self.num_appointments = num_appointments

    def __repr__(self):
        return self.__dict__.__repr__()
