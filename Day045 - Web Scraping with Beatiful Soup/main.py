# Created by Ricardo Lousada
from bs4 import BeautifulSoup
import lxml
import requests
"""
with open("website.html", encoding="UTF-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents,'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
#print(soup.prettify())
#print(soup.a)
#find all of the html elements
list_of_anchors = soup.find_all(name="a")
for tag in list_of_anchors:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section = soup.find(name="h3",class_="heading")
print(section)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

heading = soup.select(".heading")
print(heading)
"""
response = requests.get("https://news.ycombinator.com/", verify=False)

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,'html.parser')
articles= soup.find_all(name="a",rel="noreferrer")
articles_texts = []
articles_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score") ]

print(articles_texts)
print(articles_links)
print(articles_upvotes)

max_value = max(articles_upvotes)
max_index = articles_upvotes.index(max_value)
print(max_value)
print(articles_texts[max_index])
print(articles_links[max_index])
