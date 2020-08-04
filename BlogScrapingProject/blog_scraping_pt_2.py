# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])


    for article in articles:
        # find articles
        a_tag = article.find("a")
        # find titles
        title = a_tag.get_text()
        # find href
        url = a_tag['href']
        # find date/time
        date = article.find("time")["datetime"]
        
        # This ↓ is to print out the results of what we are scraping before we finalize everything onto a csv.
        # print(title, url, date)

        # This ↓ will fetch the results for our csv
        csv_writer.writerow([title, url, date])
