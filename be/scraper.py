# Indeed - Scraper v0.1
# Project scoped towards HTML Scraping not JavaScript
# Please check out Headless Browser libraries for Python such as Selenium for JavaScript Heavy Scraping
# This scraper WILL NOT work on JavaScript Heavy Websites

# import libraries
import bs4
from bs4 import BeautifulSoup
import urllib.request
import path
import json

path.appendPath()

import indeed

def scrape(url):
    # Specify the Scrape URL
    # Test URL - https://www.indeed.co.za/jobs?q=wordpress&l=Cape+Town,+Western+Cape&start=10 | https://za.indeed.com/jobs?q=javascript&l=Cape+Town%2C+Western+Cape&start=10
    # job=javascript | area=Cape Town, Western Cape | start=10

    # User-Agent
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    # Request Page
    pageQuery = urllib.request.urlopen(req)

    # Parse the HTML using BeautifulSoup
    parsedHTML = BeautifulSoup(pageQuery, 'html.parser')

    with open("parsed.html", "w", encoding="utf-8") as file:
        file.write(str(parsedHTML))

    # .encode("utf-8") | charmap error fix
    return indeed.genJSON(parsedHTML)