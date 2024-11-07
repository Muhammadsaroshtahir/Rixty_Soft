import requests
from bs4 import BeautifulSoup

with open("index.html","r") as f:
    html_doc=f.read()

soup = BeautifulSoup(html_doc,'html.parser')

# print(soup.prettify())
# print(soup.title, type(soup.title))
# print(soup.title, type(soup.title.string))
# print(soup.div)
# print (type(soup.find_all("div")[1]))

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())

# print(soup.select("div.italic"))
# print(soup.select("div#italic"))
# print(soup.span.get("class"))

# print(soup.find(class_="italic"))
# print(soup.find_all(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)

# cont =soup.find(class_="container")
# cont.name="span"
# cont["class"]="myclass class2"
# cont.string = "i am a string"
# print(cont)

#how to perpare tag
ulTag= soup.new_tag("ul")

liTag=soup.new_tag("li")
liTag.string= "Home"
ulTag.append(liTag)

litag=soup.new_tag("li")
liTag.string= "About"
ulTag.append(liTag)

soup.html.body.insert(0,ulTag)
with open("modified.html","w") as f:
    f.write(str(soup))



