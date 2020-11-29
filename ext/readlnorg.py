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
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='chapters_1-0')

    chapters = results.find('ul', class_='chapter-chs')
    chaptersList = chapters.find_all('a', class_='')

    for ch in chaptersList:
        if ch.has_attr('href'):
            print(ch.text + " : " + ch['href'])

    return ""