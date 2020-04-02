import requests
from bs4 import BeautifulSoup



def getData():
    print("getData.....")
    url = "https://bbs.ruliweb.com/market/board/1020"

    print("getData.....")

    req = requests.get(url)

    html = req.text

    #print(html)
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.select(".deco")

    print(items)

    return []

