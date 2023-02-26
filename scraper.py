import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

# Connect to the database
conn = sqlite3.connect('menu_items.db')

conn.commit()

conn.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rating REAL NOT NULL
    );
''')
             
conn.execute('DELETE FROM menu_items')
conn.execute('UPDATE sqlite_sequence SET seq=0 WHERE name="menu_items"')

campus = 0

match input("which campus?: "):
    case "busch":
        campus = 4
    case "livi":
        campus = 3
    case "neilson":
        campus = 2
    case "brower":
        campus = 1

day = input("how many days? (0 for today, up to 7 in advance):")

URL = "http://menuportal.dining.rutgers.edu/foodpro/pickmenu.asp?sName=+University+Dining&locationNum=0"
URL += str(campus)

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
mydivs = soup.find_all("div", {"class": "col-1"})

# Array to hold menu items
menu_items = []

for i in mydivs:
    menu_items.append(str(i)[96:-6])

# Cleaning the data
for i in range(len(menu_items)):
    if (menu_items[i][0] == '>'):
        menu_items[i] = menu_items[i][1:]

# Insert menu items into menu_items.db
for i in menu_items:
    conn.execute('''
        INSERT INTO menu_items (name, rating)
        VALUES (?, ?);
    ''', (i, 0))


result_set = conn.execute('SELECT * FROM menu_items')

# Fetch the results and print them
for row in result_set:
    print(row)

conn.commit()
conn.close()
