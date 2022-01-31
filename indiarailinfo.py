#!/bin/python3
def main():
    import sys

    if len(sys.argv)<2:
        print("It takes two arguments\nFirst is [normal(or regular),imaginary]\nSecond is Forum number\nExample~ ./indiarailinfo.py regular 49")

    else:
        import requests
        from bs4 import BeautifulSoup
        import fontstyle

        url1 = f"https://indiarailinfo.com/blog/{sys.argv[2]}?tp=1"
        url2 = f"https://indiarailinfo.com/blog/imaginary/{sys.argv[2]}?"

        if sys.argv[1]=="regular" or sys.argv[1]=="normal":
            url = url1
        elif sys.argv[1]=="imaginary":
            url = url2

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        print(fontstyle.apply(
            "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++", "bold/red/YELLOW_BG"))
        print(fontstyle.apply(f"| {soup.title.string} |", "bold/white/BLACK_BG"))
        print(fontstyle.apply(
            "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n", "bold/red/YELLOW_BG"))
        mygenerator = (i for i in soup.find_all(
            'a', attrs={"style": "font-weight:bold;"}))
        for i in mygenerator:
            if str(i.text) != "General Travel" and str(i.text) != "Advanced Search" and str(i.text) != "x-under SW-x" and str(i.text) != "Imaginary":
                print(fontstyle.apply(f"{i.text}\n", "bold/Italic/cyan"))

        mygen2 = (i for i in soup.find_all('h1', attrs={"class": "pinkColor"}))
        for i in mygen2:
            print(fontstyle.apply("\nQuote from a RF:", "bold/red"))
            print(fontstyle.apply(f"\n\t\t{i.text}\n\n", "italic/yellow"))

if __name__ == "__main__":
    main()
