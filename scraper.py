import requests
from bs4 import BeautifulSoup
import datetime
x = input("which campus?: ")
if (x == "busch"):
    x = 4
if (x == "livi"):
    x = 3
if (x == "neilson"):
    x = 5
if (x == "brower"):
    x = 1
y = input("how many days? (0 for today, up to 7 in advance):")
URL = "http://menuportal.dining.rutgers.edu/foodpro/pickmenu.asp?sName=+University+Dining&locationNum=0"
URL += str(x)
# results = soup.find(="col-1")
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
mydivs = soup.find_all("div", {"class": "col-1"}
                       )
thing = []
for i in mydivs:
    thing.append(str(i)[96:-6])
for i in range(len(thing)):
    if(thing[i][0] == '>'):
        thing[i] = thing[i][1:]
    # if(thing[i][0] == '/'):
    #     thing.pop(i)
    #     i -= 2
for i in thing:
    print(i)