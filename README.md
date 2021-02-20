> :warning: Update: This project is no longer being updated because of better websites like covidwa.com

# WA Covid Vaccines

Website link: https://mazore.github.io/wa-covid-vaccines

This program checks many vaccine websites for availability every couple of minutes and updates the website. You can request I add a website by adding the link to this [google doc](https://docs.google.com/document/d/1c29oy3h_LXEAy_7b93bnpQrB5mGDv5UkRzwFqydWe84/edit?usp=sharing) (try not to add duplicates). Keep in mind this is a work in progress and may not be the most reliable or accurate (the backend is just running on my computer). You can send me an email at wacovidvaccines@gmail.com.

## Coming soon
- Twitter bot that notifies you when appointments becomes available
- More websites checked
- Sorting by closest locations to you
- More details about locations

## For programmers

If you would like to contribute, I would greatly appreciate that. The main thing that I need help with is adding more websites to the program. The backend is written in python and uses a selenium webdriver to go to each website and check for availability. You can add your file to the `backend/scrapers` directory. You can look at other examples of "scrapers" in other files (I probably should make them more readable). You need to create a function named like the site name in your file, which takes in a chrome selenium webdriver `driver` and returns a `ScrapeResult` (see `backend/scrape_result.py`). Then import your function into `backend/main.py` and add it to the `all_scrapers` list. To test your function along the way, edit and run `backend/test_scraper.py`. Frontend contributions and feedback/issues are also appreciated.
