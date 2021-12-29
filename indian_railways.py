#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import fontstyle

n = int(input(fontstyle.apply("\nEnter any integer (Max Limit: 6 digits): ", "bold/Italic/green")))
url = f"https://indiarailinfo.com/blog/{n}?tp=1"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

content = soup.prettify()

print(fontstyle.apply("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++", "bold/red/YELLOW_BG"))
print(fontstyle.apply(f"| {soup.title.string} |", "bold/white/BLACK_BG"))
print(fontstyle.apply("+++++++++++++++++++++++++++++++++++++++++++++++++++\n\n", "bold/red/YELLOW_BG"))


count = 0
l=[]
for i in soup.find_all('a', attrs = {"style":"font-weight:bold;"}):
    if str(i.text) != "General Travel":
        count += 1
        l.append(i.text)

for i in range(1, count):
    print(fontstyle.apply(f"{l[i]}\n", "bold/Italic/cyan"))

print(fontstyle.apply(f"\t\toutput count: {count}", "italic/purple"))
