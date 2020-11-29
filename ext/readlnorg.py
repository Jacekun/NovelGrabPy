# imports
import requests
from bs4 import BeautifulSoup
import re
import html

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

    results = soup.find("div", {"id": "growfoodsmart"})

    if None in results:
        return ""

    retVal = str(results)
        
    # Get string after >
    try:
        target = '>'
        retVal = retVal[retVal.index(target) + len(target):]
    except:
        retVal = retVal
    
    # Relace breaks
    try:
        retVal = retVal.replace('<br>', '\n')
    except:
        retVal = retVal
    
    # Relace P tag
    try:
        retVal = retVal.replace('<p>', '\n')
    except:
        retVal = retVal

    # Relace end p tag
    try:
        retVal = retVal.replace('</p>', '')
    except:
        retVal = retVal
    
    # Encode to UTF-8
    try:
        retVal = str(retVal.encode(encoding='utf-8'))
    except:
        retVal = retVal
    
    # print(retVal)

    # return val to main App
    return retVal 