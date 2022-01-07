#!/usr/bin/python3
def main():
    import requests
    import sys
    from bs4 import BeautifulSoup
    import fontstyle
    if len(sys.argv) < 2:
        n = int(input(fontstyle.apply(
            "\nEnter any integer (Max Limit: 6 digits): ", "bold/Italic/green")))
    else:
        n = int(sys.argv[1])
    url = f"https://indiarailinfo.com/blog/{n}?tp=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    content = soup.prettify()
    print(fontstyle.apply(
        "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++", "bold/red/YELLOW_BG"))
    print(fontstyle.apply(f"| {soup.title.string} |", "bold/white/BLACK_BG"))
    print(fontstyle.apply(
        "+++++++++++++++++++++++++++++++++++++++++++++++++++\n\n", "bold/red/YELLOW_BG"))
    mygenerator = (i for i in soup.find_all(
        'a', attrs={"style": "font-weight:bold;"}))
    for i in mygenerator:
        if str(i.text) != "General Travel" and str(i.text) != "Advanced Search" and str(i.text) != "x-under SW-x":
            print(fontstyle.apply(f"{i.text}\n", "bold/Italic/cyan"))

    mygen2 = (i for i in soup.find_all('h1', attrs={"class": "pinkColor"}))
    for i in mygen2:
        print(fontstyle.apply("\nQuote from a RF:", "bold/red"))
        print(fontstyle.apply(f"\n\t\t{i.text}\n\n", "italic/yellow"))


if __name__ == "__main__":
    main()
