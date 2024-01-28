from bs4 import BeautifulSoup
import requests

with open("data/sample.html" , "r") as f:
    html_doc = f.read()
    
with open("data/quickloom.html" , "r") as f1:
    html_doc1 = f1.read()
    
soup = BeautifulSoup(html_doc , 'html.parser')
# print(soup.find(class_ = "login"))
# # print(soup.prettify())
# print(soup.title.string)

soup1 = BeautifulSoup(html_doc1 , 'html.parser')
# print(soup.prettify())
# print(soup1.find_all("a"))

# for i in soup1.find_all("a"):
#     print(i.get("href"))
# # print(soup1.select("div.container"))
# ultag = soup1.new_tag("ul")
# litag = soup1.new_tag("li")
# litag.string = "about"
# ultag.append(litag)

# soup1.html.body.insert(0 , ultag)

# with open("data/modified.html" , "w") as f:
#     f.write(str(soup1))
    
def has_class_but_not_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

results = soup1.find_all(has_class_but_not_id)
for result in results:
    print(result , "\n \n")