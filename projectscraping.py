from bs4 import BeautifulSoup
import requests

url = "https://zapier.com/blog/best-blog-sites/"

r = requests.get(url)

soup = BeautifulSoup(r.text , 'html.parser')

# print(soup.prettify())
spans = soup.select("css-r9jdok")
for span in spans:
    print(span)

