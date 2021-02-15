# Here is an example of testing the scraper for childrens hospital
from scrapers.childrens import childrens  # Import function
from selenium import webdriver  # You probably need to `pip install selenium`

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Don't pop up gui
driver = webdriver.Chrome(options=options)

print('\n', childrens(driver))
# Should output something like {'name': "Seattle Children's Hospital", 'url': ...,
# 'available': False, 'address': '4800 Sand Point Way NE Seattle, WA', 'zip': 98105, 'num_appointments': 0}
