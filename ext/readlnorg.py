# imports
import requests
from bs4 import BeautifulSoup

# global vars
page = "https://www.readlightnovel.org/"
name = "ReadLightNovel"
version = "1.0.0"
author = "Jace"

def extInfo(stringVal):
    string = "Name: " + name + "\nVersion: " + version + "\nAuthor: " + author
    return stringVal + string

def chapterLinks(URL):

    # Get number of Tabs
    tab = input("Number of Tabs: ")
    x = []

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for i in range(0, int(tab)):

        results = soup.find(id='chapters_1-'+str(i))
        chapters = results.find('ul', class_='chapter-chs')
        chaptersList = chapters.find_all('a', class_='')

        # Get the exact links, inside href
        for ch in chaptersList:
            if ch.has_attr('href'):
                x.append(ch['href'])

    return x

def getContents(URL):
    # Setup vars
    retVal = ""

    # Get body
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='growfoodsmart')

    bodyP = results.find_all('p', class_='')

    for p in bodyP:
        retVal += p.text + "\n"

    return retVal