"""10. **Basic Web Scraper**: Develop a simple web scraper to extract data from a website and store it in a file.
"""
import requests
from bs4 import BeautifulSoup

# target
web_page = "https://www.scrapethissite.com/pages/simple/"

# make a get request and parse the content 
response = requests.get(url=web_page)
soup = BeautifulSoup(response.content,"html.parser",from_encoding='Latin1')

# find all h3 tags and save content in a text file
countries = soup.find_all("h3",attrs={"class":"country-name"})
with open("web_scraper_result.txt","w") as file:
    file.write("List of countries from www.scrapethissite.com:\n\n")
    for i,country in enumerate(countries):
        file.write(f"{i+1}.-{country.text.strip()}\n")

    