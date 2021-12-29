#!/usr/bin/python3
def main():
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
    mygenerator = (i for i in soup.find_all('a', attrs = {"style":"font-weight:bold;"}))
    for i in mygenerator:
        if str(i.text) != "General Travel" and str(i.text) != "Advanced Search":
            print(fontstyle.apply(f"{i.text}\n", "bold/Italic/cyan"))

if __name__ == "__main__":
    main()